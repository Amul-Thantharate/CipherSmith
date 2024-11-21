# Local Installation Guide for PassForge

This guide will help you set up PassForge for local development.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/Amul-Thantharate/passforge.git
cd passforge
```

## Step 2: Create a Virtual Environment (Recommended)

### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Install in Development Mode

```bash
pip install -e .
```

This will install PassForge in development mode, allowing you to modify the code and test changes immediately.

## Step 5: Verify Installation

```bash
passforge --version
```

You should see the current version number of PassForge.

## Running Tests

```bash
pytest tests/
```

## Development Workflow

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test them:
   ```bash
   # Run tests
   pytest tests/
   
   # Try out your changes
   passforge [your-command]
   ```

3. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request on GitHub

## Project Structure

```
passforge/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils/
├── tests/
│   └── test_main.py
├── requirements.txt
├── setup.py
└── README.md
```

## Common Development Tasks

### Adding New Dependencies

1. Add to `requirements.txt`
2. Run:
   ```bash
   pip install -r requirements.txt
   ```

### Running Specific Tests

```bash
# Run specific test file
pytest tests/test_main.py

# Run specific test function
pytest tests/test_main.py::test_function_name

# Run with verbose output
pytest -v tests/
```

### Building Documentation

```bash
# Install documentation dependencies
pip install -r docs/requirements.txt

# Build documentation
cd docs
make html
```

## Troubleshooting

### Command Not Found
If `passforge` command is not found after installation:
1. Ensure your virtual environment is activated
2. Reinstall in development mode:
   ```bash
   pip install -e .
   ```

### Test Failures
1. Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Check Python version compatibility
3. Run tests with `-v` flag for more detail:
   ```bash
   pytest -v tests/
   ```

## Getting Help

If you encounter any issues during development:
1. Check the [GitHub Issues](https://github.com/Amul-Thantharate/passforge/issues)
2. Create a new issue with detailed information about your problem
3. Reach out to the maintainers

## Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Include docstrings for all functions and classes
- Write tests for new features

## Making a Release

1. Update version in `setup.py`
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Build and upload to PyPI:
   ```bash
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```
