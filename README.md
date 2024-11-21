# 🔐 CryptoPass

[![PyPI version](https://badge.fury.io/py/cryptopass.svg)](https://badge.fury.io/py/cryptopass)
[![Python Versions](https://img.shields.io/pypi/pyversions/cryptopass.svg)](https://pypi.org/project/cryptopass/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/cryptopass)](https://pepy.tech/project/cryptopass)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful and flexible command-line password generator that helps you create strong, secure passwords with ease. Built with security and usability in mind! 🚀

## ✨ Features

- 🎯 Generate cryptographically secure passwords
- 🔄 Customizable length and complexity
- 🎨 Include or exclude special characters, numbers, and uppercase letters
- 📋 Copy generated passwords to clipboard
- 💾 Save passwords to an encrypted file (optional)
- 🖥️ Command-line interface for easy integration into scripts
- 🔍 Password strength analysis
- 🏷️ Tag and organize passwords
- 📊 Password generation statistics
- 🔒 Secure storage using SQLite with encryption

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

#### From PyPI (Recommended)
```bash
pip install cryptopass
```

#### From Source
```bash
git clone https://github.com/Amul-Thantharate/cryptopass.git
cd cryptopass
pip install -e .
```

#### Development Installation
```bash
git clone https://github.com/Amul-Thantharate/cryptopass.git
cd cryptopass
pip install -r requirements.txt
pip install -e .[dev]
```

## 🎮 Usage

### Basic Password Generation
```bash
# Generate a default secure password
cryptopass generate

# Generate a password with specific length
cryptopass generate --length 16

# Generate a password with specific requirements
cryptopass generate --uppercase 2 --lowercase 6 --digits 2 --special 2

# Generate multiple passwords
cryptopass generate --count 5

# Save passwords to file
cryptopass generate --save passwords.txt --count 3
```

### Advanced Features
```bash
# Generate a memorable password
cryptopass generate --memorable

# Check password strength
cryptopass check "YourPassword123"
```

### Password Management
```bash
# View password history
cryptopass history

# Search passwords
cryptopass search "github"

# View statistics
cryptopass stats
```

## 📚 Documentation

For detailed documentation, visit our [Documentation Page](https://cryptopass.readthedocs.io/).

Common topics:
- [Installation Guide](LOCAL_INSTALL.md)
- [Usage Examples](DEMO.md)
- [API Reference](https://cryptopass.readthedocs.io/api)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🔧 Configuration

PassForge can be configured using:
- Command-line arguments
- Configuration file (~/.passforge/config.yaml)
- Environment variables

Example configuration:
```yaml
default_length: 16
include_special: true
save_directory: "~/passwords/"
encryption_key_file: "~/.passforge/key"
```

## 🛡️ Security

- Uses Python's `secrets` module for cryptographically secure random generation
- Implements industry-standard password security practices
- Regular security audits and updates
- No cloud storage - all data stays local
- Optional file encryption using Fernet (symmetric encryption)

## 🤝 Contributing

We love your input! We want to make contributing to PassForge as easy and transparent as possible. Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

Amul Thantharate (amulthantharate@gmail.com)

## 🌟 Support

If you find PassForge useful, please consider:
- Giving it a star on GitHub ⭐
- Sharing it with friends and colleagues
- Contributing to its development
- Reporting issues and suggesting features

## 📊 Project Status

- ✅ Actively maintained
- 🔄 Regular updates
- 📈 Growing community
- 🐛 Quick bug fixes

## 📞 Contact

- Email: amulthantharate@gmail.com
- GitHub Issues: [Report a bug](https://github.com/Amul-Thantharate/cryptopass/issues)
- Twitter: [@AmulThantharate](https://twitter.com/AmulThantharate)

## ⭐ Acknowledgments

- Thanks to all contributors
- Inspired by best practices in password security
- Built with Python's excellent cryptography libraries
