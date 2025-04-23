import curses
import os
import traceback
import sys

VERSION = "0.2.1"

class QuillEditor:
    def __init__(self, filename=None):
        self.filename = filename
        self.content = ['']  # Start with empty line for new files
        self.cursor_x = 0
        self.cursor_y = 0
        self.clipboard = ''
        self.selecting = False
        self.selection_start = (0, 0)
        if filename and os.path.exists(filename):
            with open(filename, 'r') as f:
                self.content = f.read().splitlines()

    def run(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        try:
            self._draw_interface(stdscr)
            while True:
                self._draw_interface(stdscr)
                key = stdscr.getch()
                if key == 17:  # Ctrl+Q
                    break
                elif key == 19:  # Ctrl+S
                    self.save_file(stdscr)
                    self._show_status(stdscr, "Saved!", curses.A_REVERSE)
                elif key == 3:  # Ctrl+C
                    self._copy_to_clipboard(stdscr)
                elif key == 22:  # Ctrl+V
                    self._paste_from_clipboard(stdscr)
                elif key == curses.KEY_UP:
                    self.cursor_y = max(0, self.cursor_y-1)
                elif key == curses.KEY_DOWN:
                    self.cursor_y = min(len(self.content)-1, self.cursor_y+1)
                elif key == curses.KEY_LEFT:
                    self.cursor_x = max(0, self.cursor_x-1)
                elif key == curses.KEY_RIGHT:
                    self.cursor_x = min(len(self.content[self.cursor_y]), self.cursor_x+1)
                elif key in (curses.KEY_BACKSPACE, 127, 8):  # Handle all backspace variations (ASCII DEL/BS, curses constant)
                    if self.cursor_x > 0:
                        # Delete within current line
                        self.content[self.cursor_y] = self.content[self.cursor_y][:self.cursor_x-1] + self.content[self.cursor_y][self.cursor_x:]
                        self.cursor_x -= 1
                    elif self.cursor_y > 0:
                        # Merge with previous line when at start of line
                        prev_line_length = len(self.content[self.cursor_y - 1])
                        self.content[self.cursor_y - 1] += self.content[self.cursor_y]
                        del self.content[self.cursor_y]
                        self.cursor_y -= 1
                        self.cursor_x = prev_line_length
                elif key == 10:  # Enter
                    self.content.insert(self.cursor_y+1, self.content[self.cursor_y][self.cursor_x:])
                    self.content[self.cursor_y] = self.content[self.cursor_y][:self.cursor_x]
                    self.cursor_y += 1
                    self.cursor_x = 0
                elif 32 <= key <= 126:  # Printable characters
                    self.content[self.cursor_y] = self.content[self.cursor_y][:self.cursor_x] + chr(key) + self.content[self.cursor_y][self.cursor_x:]
                    self.cursor_x += 1
        finally:
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()

    def save_file(self, stdscr):
        if not self.filename:
            curses.echo()
            height, width = stdscr.getmaxyx()
            stdscr.move(height-2, 0)
            stdscr.clrtoeol()
            stdscr.addstr(height-2, 0, "Enter filename: ")
            curses.echo()
            self.filename = stdscr.getstr(height-2, 14, 60).decode('utf-8').strip()
            curses.noecho()
            if not self.filename:
                self._show_status(stdscr, "Save canceled", curses.A_REVERSE)
                return
            curses.noecho()
        
        directory = os.path.dirname(self.filename)
        if directory:  # Only create directories if path exists
            os.makedirs(directory, exist_ok=True)
        with open(self.filename, 'w') as f:
            f.write('\n'.join(self.content))

    def _show_status(self, stdscr, message, style=curses.A_NORMAL):
        height, width = stdscr.getmaxyx()
        status_bar = message.ljust(width-1)
        stdscr.addstr(height-2, 0, status_bar, style)
        stdscr.refresh()
        stdscr.timeout(1000)  # Display message for 1 second
        stdscr.getch()  # Wait for any key press or timeout
        self._draw_interface(stdscr)

    def _draw_interface(self, stdscr):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        # Display content with selection highlighting
        for y, line in enumerate(self.content[:height-2]):
            if self.selecting:
                start_y, start_x = self.selection_start
                end_y, end_x = (self.cursor_y, self.cursor_x)
                if start_y > end_y or (start_y == end_y and start_x > end_x):
                    start_y, start_x, end_y, end_x = end_y, end_x, start_y, start_x
                
                if y == start_y == end_y:
                    stdscr.addstr(y, 0, line[:start_x])
                    stdscr.addstr(y, start_x, line[start_x:end_x], curses.A_REVERSE)
                    stdscr.addstr(y, end_x, line[end_x:width-1])
                elif start_y <= y <= end_y:
                    if y == start_y:
                        stdscr.addstr(y, 0, line[:start_x])
                        stdscr.addstr(y, start_x, line[start_x:width-1], curses.A_REVERSE)
                    elif y == end_y:
                        stdscr.addstr(y, 0, line[:end_x], curses.A_REVERSE)
                        stdscr.addstr(y, end_x, line[end_x:width-1])
                    else:
                        stdscr.addstr(y, 0, line[:width-1], curses.A_REVERSE)
                else:
                    stdscr.addstr(y, 0, line[:width-1])
            else:
                stdscr.addstr(y, 0, line[:width-1])
        
        # Show status bar
        status_bar = f"QuillPy - {self.filename}" if self.filename else "QuillPy - New File"
        stdscr.addstr(height-1, 0, status_bar.ljust(width-1))
        
        # Position cursor
        stdscr.move(min(self.cursor_y, height-3), min(self.cursor_x, width-2))
        stdscr.refresh()

    def _copy_to_clipboard(self, stdscr):
        if self.selecting:
            start_y, start_x = self.selection_start
            end_y, end_x = (self.cursor_y, self.cursor_x)
            if start_y > end_y or (start_y == end_y and start_x > end_x):
                start_y, start_x, end_y, end_x = end_y, end_x, start_y, start_x
            
            selected_lines = self.content[start_y:end_y+1]
            if len(selected_lines) == 1:
                self.clipboard = selected_lines[0][start_x:end_x]
            else:
                selected_lines[0] = selected_lines[0][start_x:]
                selected_lines[-1] = selected_lines[-1][:end_x]
                self.clipboard = '\n'.join(selected_lines)
            
            try:
                import win32clipboard
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(self.clipboard)
                win32clipboard.CloseClipboard()
                self._show_status(stdscr, "Copied to clipboard!", curses.A_REVERSE)
            except ImportError:
                self._show_status(stdscr, "Clipboard: Install pywin32 for system access", curses.A_REVERSE)
                self.clipboard = self.clipboard  # Store in internal clipboard
            except Exception as e:
                self._show_status(stdscr, f"Clipboard error: {str(e)}", curses.A_REVERSE)
                self.clipboard = selected_text  # Fallback to internal clipboard)
        else:
            self._show_status(stdscr, "No selection to copy", curses.A_REVERSE)

    def _paste_from_clipboard(self, stdscr):
        try:
            import win32clipboard
            win32clipboard.OpenClipboard()
            pasted = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
        except ImportError:
            pasted = self.clipboard
            self._show_status(stdscr, "Using internal clipboard - install pywin32 for system access", curses.A_REVERSE)
        except Exception as e:
            self._show_status(stdscr, f"Clipboard error: {str(e)}", curses.A_REVERSE)
            pasted = self.clipboard  # Fallback to internal clipboard
            return
        
        if pasted:
            lines = pasted.split('\n')
            current_line = self.content[self.cursor_y]
            self.content[self.cursor_y] = current_line[:self.cursor_x] + lines[0] + current_line[self.cursor_x:]
            for line in reversed(lines[1:]):
                self.content.insert(self.cursor_y+1, line)
            self.cursor_x += len(lines[0])
            self.cursor_y += len(lines)-1
            self._show_status(stdscr, "Pasted from clipboard!", curses.A_REVERSE)
        else:
            self._show_status(stdscr, "Clipboard is empty", curses.A_REVERSE)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    editor = QuillEditor(filename)
    editor.run()

def colour(code, text):
    return(f"{code}{text}\033[0m")

if __name__ == "__main__":
    try:
        if len(sys.argv) = 1:
            if sys.argv[1].lower() == "version":
                print(f"Version: v{VERSION}")
        main()
    except Exception as e:
        print(colour('\033[31m', 'Oh no! An error occurred!.'))
        if not str(e):
            print(colour('\033[31m', f'Basic data: {str(e)}'))
        else:
            print(colour('\033[31m', 'No basic data available.'))
        try:
            full_tb = traceback.format_exc()
            if input(colour('\033[33m', 'View full Traceback? (Put in error report) (y/n)')).strip().lower() != "y":
                print(colour('\033[31m', 'Not viewing full traceback.'))
                exit(1)
            print(colour('\033[31m', 'Full traceback:'))
            print(colour('\033[35m', full_tb))
        except Exception as e2:
            print(colour('\033[31m', f"An error occurred generating full traceback: {e2}."))
