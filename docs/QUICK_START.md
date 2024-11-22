---
layout: default
title: Quick Start Guide
permalink: /CipherSmith/QUICK_START
---

# 🚀 CipherSmith Quick Start Guide

Get up and running with CipherSmith in minutes!

## 📦 Installation

### 1. Using pip
```bash
pip install CipherSmith
```

### 2. Verify Installation
```bash
CipherSmith --version
```

## 🎯 Basic Usage

### 1. Generate a Password
```bash
# Generate a 16-character password
CipherSmith generate -t 16
```

### 2. Check Password Strength
```bash
CipherSmith check "YourPassword123"
```

### 3. View History
```bash
CipherSmith history
```

## 🔥 Common Tasks

### Password Generation

#### Simple Password
```bash
# 12-character password
CipherSmith generate -t 12
```

#### Complex Password
```bash
# 16 chars with specific requirements
CipherSmith generate -n 4 -l 4 -u 4 -s 4
```

#### Multiple Passwords
```bash
# Generate 5 passwords
CipherSmith generate -t 16 -a 5
```

### Password Management

#### Add Tags
```bash
CipherSmith generate -t 16 --tag work --tag important
```

#### Search History
```bash
CipherSmith search "work"
```

#### Clear Old Passwords
```bash
CipherSmith clear --days 30
```

## 🛠️ Tips & Tricks

### 1. Password Generation
- Use `-e` to exclude similar characters
- Add descriptions with `--description`
- Save to file with `-o filename.txt`

### 2. History Management
- Filter by tags
- Limit output with `--limit`
- Use search for finding specific entries

### 3. Password Analysis
- Use verbose mode for detailed analysis
- Check against common patterns
- Get crack time estimates

## 🎨 Customization

### Environment Variables
```bash
# Set custom database location
export CIPHERSMITH_DB_PATH="/path/to/db"
```

### Configuration Options
- Custom character sets
- Output formatting
- History retention

## 🔍 Common Issues

### 1. Installation Problems
```bash
# Update pip
python -m pip install --upgrade pip

# Install in user space
pip install --user CipherSmith
```

### 2. Permission Issues
```bash
# Check database permissions
ls -l ~/.secure_passgen/

# Fix permissions
chmod 600 ~/.secure_passgen/passwords.db
```

### 3. Common Errors
- Database connection issues
- Invalid character combinations
- Permission denied errors

## 📚 Next Steps

1. Read the full [documentation](./README.md)
2. Check out [advanced features](./API_REFERENCE.md)
3. Join our [community](https://github.com/Amul-Thantharate/CipherSmith/discussions)

## 🆘 Getting Help

- Use `--help` with any command
- Check our [FAQ](./README.md#frequently-asked-questions)
- Open an [issue](https://github.com/Amul-Thantharate/CipherSmith/issues)

---
📅 Last Updated: March 20, 2024  
🔄 Version: 1.3.0
