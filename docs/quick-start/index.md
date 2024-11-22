---
layout: default
title: Quick Start Guide
permalink: /CipherSmith/quick-start/
---

# 🚀 CipherSmith Quick Start Guide

Get up and running with CipherSmith in minutes!

## 📦 Installation

```bash
pip install ciphersmith
```

## 🎯 Basic Usage

### Generate a Password

```bash
# Generate a 16-character password
ciphersmith generate --total-length 16

# Generate with specific requirements
ciphersmith generate --lowercase 8 --uppercase 4 --numbers 2 --special-chars 2

# Generate multiple passwords
ciphersmith generate --amount 5 --total-length 12
```

### Check Password Strength

```bash
# Basic strength check
ciphersmith check "YourPassword123!"

# Detailed analysis
ciphersmith check --verbose "YourPassword123!"
```

### View Password History

```bash
# View recent passwords
ciphersmith history

# View with limit
ciphersmith history --limit 5

# Filter by tag
ciphersmith history --tag "work"
```

### Search History

```bash
# Search by description or tags
ciphersmith search "project"
```

## 🔧 Configuration

### Character Sets

- Lowercase: a-z
- Uppercase: A-Z
- Numbers: 0-9
- Special: !@#$%^&*()_+-=[]{}|;:,.<>?

### Password Requirements

- Minimum Length: 8 characters
- Maximum Length: 128 characters
- Default Length: 16 characters

## 🎨 Examples

### Strong Password for Work

```bash
ciphersmith generate \
    --total-length 20 \
    --lowercase 8 \
    --uppercase 6 \
    --numbers 4 \
    --special-chars 2 \
    --description "Work account" \
    --tags "work,important" \
    --check-strength
```

### Multiple Passwords for Testing

```bash
ciphersmith generate \
    --amount 10 \
    --total-length 12 \
    --output-file "test_passwords.txt" \
    --description "Test accounts" \
    --tags "test,temporary"
```

### Password Analysis

```bash
ciphersmith check --verbose "MyP@ssw0rd!" \
    --save-history \
    --description "Example password" \
    --tags "example,demo"
```

## 🔒 Security Tips

1. **Use Long Passwords**
   - Aim for at least 16 characters
   - Mix different character types

2. **Avoid Common Patterns**
   - Don't use keyboard patterns (qwerty)
   - Avoid common substitutions (@ for a)

3. **Regular Updates**
   - Change passwords periodically
   - Don't reuse passwords

4. **Safe Storage**
   - Use the built-in history feature
   - Keep your database secure

## 🛠️ Advanced Features

### Custom Character Sets

```bash
# Exclude similar characters
ciphersmith generate --exclude-similar --total-length 16

# No special characters
ciphersmith generate --no-specials --total-length 16
```

### History Management

```bash
# Clear old entries
ciphersmith clear --days 30

# Force clear all history
ciphersmith clear --force
```

### Output Options

```bash
# Save to file
ciphersmith generate --output-file "passwords.txt"

# Verbose output
ciphersmith generate --verbose
```

## 📚 Next Steps

1. Explore the [API Reference](/CipherSmith/api-reference/) for detailed documentation
2. Check the [Changelog](/CipherSmith/changelog/) for updates
3. Try the interactive demo at [Examples](/CipherSmith/examples/)

## 🆘 Need Help?

- File issues on [GitHub](https://github.com/Amul-Thantharate/CipherSmith/issues)
- Check the [API Reference](/CipherSmith/api-reference/) for detailed documentation
- Review the [Changelog](/CipherSmith/changelog/) for recent updates
