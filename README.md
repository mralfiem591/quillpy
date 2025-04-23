<div align="center">
    <img src="https://github.com/mralfiem591/quillpy/raw/1fba968964a17ea39e31a43e4bf51a2bd90b9d3f/logo.png" alt="QuillPy Logo" width="400">
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

**View Version**

To view the version of QuillPy, run it like normal, but for the path, specify "version". Example:
```bash
quillpy version
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

## Development Setup

```bash
python -m pip install -e .
```

Please follow PEP8 guidelines and include tests with any changes.
