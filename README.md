# 🔐 CipherSmith

[![PyPI version](https://badge.fury.io/py/CipherSmith.svg)](https://badge.fury.io/py/CipherSmith)
[![Python Versions](https://img.shields.io/pypi/pyversions/CipherSmith.svg)](https://pypi.org/project/CipherSmith/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/CipherSmith)](https://pepy.tech/project/CipherSmith)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful and flexible command-line password generator with real-time strength analysis. Built with security and usability in mind! 🚀

## ✨ Features

- 🎯 Generate cryptographically secure passwords
- 🔄 Customizable length and complexity
- 🎨 Include or exclude special characters, numbers, and uppercase letters
- 📋 Copy generated passwords to clipboard
- 💾 Save passwords to an encrypted file (optional)
- 🖥️ Command-line interface for easy integration
- 🔍 Advanced password strength analysis
- 🏷️ Tag and organize passwords
- 📊 Password generation statistics
- 🔒 Secure storage using SQLite with encryption
- 📈 Real-time strength visualization
- ⚡ Crack time estimation
- 🎯 Pattern detection and feedback

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

# Generate and analyze password strength
CipherSmith generate --check-strength

# Check existing password strength
CipherSmith check "YourPassword123"

# Generate password with specific requirements
CipherSmith generate --uppercase 2 --lowercase 6 --digits 2 --special 2

# Save passwords to file
CipherSmith generate --save passwords.txt --count 3
```

## 🔍 Password Strength Analysis

CipherSmith now includes advanced password strength analysis:

- Real-time strength visualization
- Pattern detection
- Crack time estimation
- Security suggestions
- Comprehensive feedback

Example output:
```
Password Strength Analysis

Strength: Strong ██████████████████░░ 80%

Estimated crack time: 3 centuries

Issues Found:
✗ Contains common word pattern
✗ Predictable character substitutions

Suggestions:
• Use more unique character combinations
• Avoid common word patterns
• Add special characters
```

## 📚 Documentation

For detailed documentation, visit our [Documentation Page](https://CipherSmith.readthedocs.io/).

Common topics:
- [Installation Guide](LOCAL_INSTALL.md)
- [Usage Examples](DEMO.md)
- [API Reference](https://CipherSmith.readthedocs.io/api)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star Us!

If you find CipherSmith helpful, please consider giving us a star on GitHub! It helps us know that you find the project useful.
