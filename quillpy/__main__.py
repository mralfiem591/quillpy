from .quill import QuillEditor, main
import traceback

VERSION = "0.2.6"

def colour(code, text):
    return(f"{code}{text}\033[0m")

if __name__ == "__main__":
    try:
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
