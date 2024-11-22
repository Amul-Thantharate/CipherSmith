# 🔐 CipherSmith Documentation

Welcome to CipherSmith - Your Advanced Password Management Solution! 

## 📚 Table of Contents
- [Introduction](#-introduction)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Command Reference](#-command-reference)
- [Advanced Usage](#-advanced-usage)
- [Best Practices](#-best-practices)
- [Contributing](#-contributing)
- [FAQ](#-frequently-asked-questions)

## 🎯 Introduction

CipherSmith is a powerful command-line password manager that helps you generate, analyze, and manage secure passwords. Built with Python and modern security practices, it offers:

- 🛡️ Strong password generation with customizable options
- 📊 Real-time password strength analysis
- 📝 Password history management
- 🏷️ Tag-based organization
- 🔍 Advanced search capabilities

## ✨ Features

### Password Generation
- Custom length and character sets
- Exclude similar characters
- Batch password generation
- Configurable complexity rules

### Password Analysis
- Real-time strength checking
- Comprehensive security feedback
- Common pattern detection
- Estimated crack time calculation

### History Management
- Track password generations
- Filter by tags and dates
- Search functionality
- Export capabilities

## 📦 Installation

### Using pip (Recommended)
```bash
pip install CipherSmith
```

### From Source
```bash
git clone https://github.com/Amul-Thantharate/CipherSmith.git
cd CipherSmith
pip install -e .
```

### Requirements
- Python 3.9 or higher
- See requirements.txt for dependencies

## 🚀 Quick Start

### Generate a Password
```bash
CipherSmith generate -t 16  # Generate 16-character password
```

### Check Password Strength
```bash
CipherSmith check "YourPassword123"
```

### View Password History
```bash
CipherSmith history
```

## 📖 Command Reference

### generate
Generate secure passwords with various options:
```bash
# Basic usage
CipherSmith generate -t 12

# With specific character counts
CipherSmith generate -n 3 -l 5 -u 3 -s 2

# Generate multiple passwords
CipherSmith generate -t 16 -a 5

# Exclude similar characters
CipherSmith generate -t 12 -e
```

### check
Analyze password strength:
```bash
# Basic check
CipherSmith check "YourPassword123"

# Detailed analysis
CipherSmith check "YourPassword123" -v
```

### history
Manage password history:
```bash
# View recent history
CipherSmith history

# Filter by tag
CipherSmith history --tag work

# Limit entries
CipherSmith history --limit 5
```

### search
Search through password history:
```bash
# Search by description
CipherSmith search "website"

# Limit search results
CipherSmith search "email" --limit 3
```

### clear
Clear password history:
```bash
# Clear all history
CipherSmith clear

# Clear older entries
CipherSmith clear --days 30
```

## 🔧 Advanced Usage

### Custom Character Sets
```bash
CipherSmith generate --no-specials -t 16  # No special characters
```

### Tags and Organization
```bash
CipherSmith generate -t 16 --tag work --tag important
```

### Password Strength Requirements
- Minimum length: 8 characters
- Recommended: Mix of uppercase, lowercase, numbers, and special characters
- Avoid common patterns and dictionary words

## 🌟 Best Practices

1. 🔒 Regular Password Updates
   - Change passwords every 90 days
   - Don't reuse passwords across services

2. 📝 Password Storage
   - Use the built-in history feature responsibly
   - Clear old entries regularly

3. 🎯 Password Complexity
   - Use maximum allowed length
   - Include all character types
   - Avoid personal information

## 👥 Contributing

We welcome contributions! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

### Development Setup
1. Fork the repository
2. Create a virtual environment
3. Install development dependencies
4. Run tests before submitting PR

## ❓ Frequently Asked Questions

### Q: How secure are the generated passwords?
A: CipherSmith uses Python's `secrets` module for cryptographically strong random generation.

### Q: Where are passwords stored?
A: Passwords are stored locally in an encrypted SQLite database in your home directory.

### Q: Can I export my password history?
A: Yes, use the history command with output redirection.

## 🔗 Links
- [GitHub Repository](https://github.com/Amul-Thantharate/CipherSmith)
- [Issue Tracker](https://github.com/Amul-Thantharate/CipherSmith/issues)
- [PyPI Package](https://pypi.org/project/CipherSmith/)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---
📅 Last Updated: March 20, 2024  
🔄 Version: 1.3.0
