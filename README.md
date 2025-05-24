[![Python Tests](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/python-test.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/python-test.yml)
[![Python Build Package](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/python-build.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/actions/workflows/python-build.yml)

# modosaurus
```
usage: modosaurus [-h] [-v] N [N ...]

A tool to match groups of notes to possible scales

positional arguments:
  N              A note (e.g. Ab, E#, G)

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

The script has been updated to modern Python 3 standards for improved readability and maintainability.

## Development

### Setup
It's recommended to use a virtual environment.

To install the package and its development dependencies:
```bash
pip install -e .
```

### Running Tests
To run the unit tests:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

### Building the Package
To build the package (sdist and wheel):
```bash
pip install build
python -m build
```
The built packages will be in the `dist/` directory.
