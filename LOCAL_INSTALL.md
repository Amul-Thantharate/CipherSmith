# 🛠️ Local Installation Guide for SecureKey

This guide provides detailed instructions for setting up SecureKey in your local development environment.

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Git
- Virtual environment tool (recommended)

## 📥 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/Amul-Thantharate/CipherSmith.git
cd SecureKey
```

### 2. Create a Virtual Environment

#### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install all dependencies including development tools
pip install -r requirements.txt

# For production dependencies only
pip install .
```

### 4. Install in Development Mode

```bash
pip install -e .
```

This installs CipherSmith in development mode, allowing you to modify the code and test changes immediately.

## 📁 Project Structure

```
CipherSmith/
├── app/                    # Main application code
│   ├── __init__.py
│   ├── main.py            # CLI and core functionality
│   └── database.py        # Database operations
├── tests/                 # Test suite
│   └── test_main.py      # Main test file
├── dist/                  # Distribution files
├── .gitignore            # Git ignore patterns
├── CHANGELOG.md          # Version history
├── DEMO.md               # Usage examples
├── LICENSE               # MIT License
├── LOCAL_INSTALL.md      # This file
├── MANIFEST.ini          # Package manifest
├── README.md             # Project overview
├── pyproject.toml        # Project configuration
├── requirements.txt      # Project dependencies
└── setup.py             # Package setup
```

## 🧪 Development Tools

### Code Formatting and Linting

```bash
# Format code with black
black app/ tests/

# Sort imports
isort app/ tests/

# Run type checking
mypy app/

# Run linting
flake8 app/ tests/
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app

# Run specific test file
pytest tests/test_main.py

# Run specific test function
pytest tests/test_main.py::test_function_name
```

## 🔧 Configuration

### Development Configuration
- Edit `pyproject.toml` for tool configurations
- Modify `setup.py` for package metadata
- Update `requirements.txt` for dependencies

### Application Configuration
Default configuration location: `~/.SecureKey/config.yaml`

Example configuration:
```yaml
default_length: 16
include_special: true
save_directory: "~/passwords/"
encryption_key_file: "~/.SecureKey/key"
```

## 🐛 Troubleshooting

### Common Issues

1. **Command Not Found**
   ```bash
   # Ensure virtual environment is activated
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # Linux/macOS
   
   # Reinstall in development mode
   pip install -e .
   ```

2. **Import Errors**
   ```bash
   # Verify all dependencies are installed
   pip install -r requirements.txt
   
   # Check Python version
   python --version
   ```

3. **Test Failures**
   ```bash
   # Run tests with verbose output
   pytest -v
   
   # Check test coverage
   pytest --cov=app --cov-report=term-missing
   ```

## 📦 Building for Distribution

```bash
# Install build tools
pip install build twine

# Build distribution packages
python -m build

# Check distribution packages
twine check dist/*

# Upload to TestPyPI (optional)
twine upload --repository testpypi dist/*
```

## 🔄 Git Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make changes and test:
   ```bash
   # Run all checks
   black app/ tests/
   isort app/ tests/
   mypy app/
   pytest
   ```

3. Commit changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. Push changes:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request on GitHub

## 📚 Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Black Documentation](https://black.readthedocs.io/)
- [mypy Documentation](https://mypy.readthedocs.io/)

## 🤝 Getting Help

- Check [GitHub Issues](https://github.com/Amul-Thantharate/SecureKey/issues)
- Join discussions in the repository
- Contact maintainers: amulthantharate@gmail.com

## 🔒 Security

When developing new features, ensure:
- Use `secrets` module for cryptographic operations
- Follow secure coding practices
- Never commit sensitive data
- Keep dependencies updated

## ✅ Pre-commit Checks

Install pre-commit hooks:
```bash
pre-commit install
```

This will automatically:
- Format code (black)
- Sort imports (isort)
- Check types (mypy)
- Run linting (flake8)
- Check for sensitive data
