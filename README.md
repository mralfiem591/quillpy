<div align="center">
    <img src="https://raw.githubusercontent.com/mralfiem591/quillpy/7c487a5d1142ceeccb12a856646b2712809dd541/logo.png" alt="QuillPy Logo" width="400">
</div>

# QuillPy

[![Publish Python Package](https://github.com/mralfiem591/quillpy/actions/workflows/python-publish.yml/badge.svg)](https://github.com/mralfiem591/quillpy/actions/workflows/python-publish.yml)
[![CodeQL](https://github.com/mralfiem591/quillpy/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/mralfiem591/quillpy/actions/workflows/github-code-scanning/codeql)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Made_with-Python-blue)
![GitHub stars](https://img.shields.io/github/stars/mralfiem591/quillpy)
![GitHub issues](https://img.shields.io/github/issues/mralfiem591/quillpy)
![PyPI downloads](https://img.shields.io/pypi/dm/quillpy)


A lightweight terminal-based text editor for Python

## Installation

```bash
# Install from PyPI
pip install quillpy

```

## Usage

```bash
quillpy filename.txt  # Open existing file
quillpy newfile.txt    # Create new file
```

If that dosen't work, try:

```bash
python -m quillpy filename.txt  # Open existing file
python -m quillpy newfile.txt    # Create new file
```

**Key Bindings:**

- Ctrl+S: Save file
- Ctrl+Q: Quit editor
- Ctrl+C: Copy selection
- Ctrl+V: Paste clipboard
- Arrow keys: Navigation
- Backspace: Delete previous character
- Enter: Insert newline

## Features

- Cross-platform terminal UI
- Basic text editing operations
- Syntax highlighting (Python supported)
- Multiple file support
- Clipboard support (Windows)

## License

[MIT License](LICENSE)
Copyright 2025 mralfiem591

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Development Setup

```bash
python -m pip install -e .
```

Please follow PEP8 guidelines and include tests with any changes.
