# Contributing to CipherSmith 🔐

First off, thank you for considering contributing to CipherSmith! It's people like you that make CipherSmith such a great tool.

## Code of Conduct 📜

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Exercise consideration and empathy
- Focus on what is best for the community
- Use welcoming and inclusive language

## How Can I Contribute? 🤝

### Reporting Bugs 🐛

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

1. **Use a clear and descriptive title**
2. **Describe the exact steps to reproduce the problem**
3. **Provide specific examples**
4. Include:
   - Your Python version
   - CipherSmith version
   - Operating system
   - Error messages (if any)
   - Screenshots (if applicable)

### Suggesting Enhancements ✨

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

1. **Use a clear and descriptive title**
2. **Provide a step-by-step description of the suggested enhancement**
3. **Explain why this enhancement would be useful**
4. **List some examples of how it would be used**

### Pull Requests 📥

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Run tests:
   ```bash
   pytest
   ```
5. Update documentation if needed
6. Commit your changes:
   ```bash
   git commit -m "feat: Add some feature"
   ```
   Follow our commit message conventions:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `test:` for test changes
   - `refactor:` for code refactoring
   - `style:` for formatting changes
   - `chore:` for maintenance tasks

7. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
8. Open a Pull Request

## Development Setup 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/CipherSmith.git
   cd CipherSmith
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in development mode
   ```

4. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Code Style 🎨

- Follow PEP 8 guidelines
- Use [Black](https://github.com/psf/black) for code formatting
- Use type hints where possible
- Write docstrings for functions and classes
- Add comments for complex logic

## Testing 🧪

- Write tests for new features
- Ensure all tests pass before submitting PR
- Maintain or improve code coverage
- Run tests with:
  ```bash
  pytest
  pytest --cov=ciphersmith  # For coverage report
  ```

## Documentation 📚

- Update documentation for new features
- Include docstrings in code
- Update README.md if needed
- Add examples for new functionality

## Project Structure 📁

```
CipherSmith/
├── ciphersmith/           # Main package directory
│   ├── __init__.py
│   ├── cli.py            # Command line interface
│   ├── generator.py      # Password generation logic
│   └── analyzer.py       # Password analysis logic
├── tests/                # Test directory
├── docs/                 # Documentation
├── requirements.txt      # Production dependencies
└── requirements-dev.txt  # Development dependencies
```

## Need Help? 🤔

Feel free to:
- Open an issue with your question
- Join our discussions
- Contact maintainers

## Recognition 🌟

Contributors will be:
- Listed in our README.md
- Mentioned in release notes
- Added to contributors list

Thank you for contributing to CipherSmith! 🙏
