# 🔐 CipherSmith

[![PyPI version](https://badge.fury.io/py/CipherSmith.svg)](https://badge.fury.io/py/CipherSmith)
[![Python Versions](https://img.shields.io/pypi/pyversions/CipherSmith.svg)](https://pypi.org/project/CipherSmith/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful CLI password generator with real-time strength analysis and advanced security features. Built with security and usability in mind! 🚀

## ✨ Features

- 🎯 Generate cryptographically secure passwords
- 📊 Real-time password strength analysis using zxcvbn
- 🔍 Detailed password security feedback and suggestions
- 📝 Password history tracking with tags and descriptions
- 🔎 Search through password history
- 📈 Password generation statistics
- 🎨 Exclude similar characters option
- 🛡️ Advanced pattern detection and security analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

```bash
pip install CipherSmith
```

### Basic Usage

```bash
# Generate a secure password
CipherSmith generate

# Generate with specific requirements
CipherSmith generate --uppercase 2 --lowercase 6 --numbers 2 --special-chars 2

# Check password strength
CipherSmith check "your-password-here"

# Check with detailed analysis
CipherSmith check "your-password-here" --verbose

# View password history
CipherSmith history

# Search passwords
CipherSmith search "github"
```

## 🔍 Password Strength Analysis

CipherSmith includes advanced password strength analysis:

- Real-time strength visualization
- Pattern detection
- Crack time estimation
- Security suggestions
- Comprehensive feedback

Example output:
```
Password Strength Analysis:
Score: 4/4
Crack Time: 1961.20 seconds
Feedback: Strong password!

Additional Details:
Length: 18
Character Sets: lowercase, uppercase, numbers, special
Patterns Found: None
Suggestions: None
```

## 📚 Documentation

For detailed usage examples, see our [Demo Guide](DEMO.md).

Common topics:
- [Installation Guide](INSTALL.md)
- [Usage Examples](DEMO.md)
- [Changelog](CHANGELOG.md)

## 🔧 Dependencies

- typer>=0.9.0
- rich>=10.0.0
- zxcvbn-python>=4.4.24
- cryptography>=41.0.0
- sqlalchemy>=2.0.0
- click>=8.0.0
- colorama>=0.4.4

## 📦 Versioning and Releases

When you've added new features or made changes to the code, follow these steps to create a new release:

1. Update version number in `pyproject.toml`:
   ```toml
   [tool.poetry]
   version = "x.y.z"  # Increment according to semantic versioning
   ```

2. Create and push a new tag:
   ```bash
   # Create a new tag
   git tag -a v1.2.3 -m "Release version 1.2.3"
   
   # Push the tag
   git push origin v1.2.3
   ```

   Version numbering follows [Semantic Versioning](https://semver.org/):
   - MAJOR version (x) - Incompatible API changes
   - MINOR version (y) - Added functionality (backwards-compatible)
   - PATCH version (z) - Bug fixes (backwards-compatible)

3. The GitHub Actions workflow will automatically:
   - Build the Python package
   - Sign the package using Sigstore
   - Create a GitHub release
   - Upload the signed distribution packages

4. The release will be available on:
   - GitHub Releases page
   - PyPI (after successful publication)

Example scenarios:
- Added new command: `v1.1.0`
- Fixed a bug: `v1.0.1`
- Breaking change: `v2.0.0`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Author

Amul Thantharate (amulthantharate@gmail.com)

## 🔄 Version

Current version: 1.2.0
