# QuillPy

A lightweight terminal-based text editor for Python

## Installation

```bash
# Install from PyPI
pip install quillpy

# Install with clipboard support (Windows)
pip install quillpy[windows]

# Development install
pip install -e .
```

## Development Setup

```bash
git clone https://github.com/yourusername/quillpy
cd quillpy
pip install -e .[dev]
```

## Usage

```bash
quillpy filename.txt  # Open existing file
quillpy newfile.txt    # Create new file
```

**Key Bindings:**

- Ctrl+S: Save file
- Ctrl+Q: Quit editor
- Ctrl+C: Copy selection
- Ctrl+V: Paste clipboard
- Arrow keys: Navigation
- Backspace: Delete previous character
- Enter: Insert newline

## Publishing to PyPI

```bash
# Install build tools
pip install setuptools wheel twine

# Build package
python setup.py sdist bdist_wheel

# Upload to PyPI
python -m twine upload dist/*
```

## Features

- Cross-platform terminal UI
- Basic text editing operations
- Syntax highlighting (Python supported)
- Multiple file support

## Dependencies

- pywin32 (Windows only) - For system clipboard integration
- windows-curses (Windows only) - For terminal UI support

## Development

```bash
python -m pip install -e .
```

## Contributing

Pull requests welcome! Please follow PEP8 guidelines and include tests.
