# CipherSmith Demo Guide

This guide demonstrates the key features of CipherSmith with practical examples.

## 1. Basic Password Generation

Generate a secure password with default settings:
```bash
CipherSmith generate
```

Generate multiple passwords:
```bash
CipherSmith generate --amount 5
```

## 2. Password Strength Analysis

Check strength of an existing password:
```bash
CipherSmith check "MyPassword123"
```

Generate password with strength analysis:
```bash
CipherSmith generate --check-strength
```

## 3. Customized Password Generation

Generate password with specific requirements:
```bash
CipherSmith generate --length 16 --uppercase 2 --lowercase 8 --digits 3 --special 3
```

Generate memorable password:
```bash
CipherSmith generate --memorable
```

## 4. Password Management

Save passwords to file:
```bash
CipherSmith generate --save passwords.txt --amount 3
```

View password history:
```bash
CipherSmith history
```

Search saved passwords:
```bash
CipherSmith search "github"
```

## 5. Advanced Features

### Password Strength Visualization

The strength meter shows:
- Overall strength score (0-4)
- Visual progress bar
- Estimated crack time
- Pattern detection
- Security suggestions

Example output:
```
Password: Tr0ub4dour&3

Strength Analysis:
█████████████████░░░ 75%
Score: 3/4 (Strong)

Estimated crack time: 
- Online attack: centuries
- Offline attack: decades

Patterns detected:
✓ Good length
✓ Mixed case
✓ Numbers and symbols
⚠️ Common substitutions (a->4)

Suggestions:
• Avoid common word patterns
• Use more unique characters
```

### Statistics

View password generation stats:
```bash
CipherSmith stats
```

Example output:
```
Password Statistics:
- Total generated: 42
- Average length: 14.3
- Most common length: 16
- Strength distribution:
  • Very weak: 5%
  • Weak: 15%
  • Medium: 30%
  • Strong: 35%
  • Very strong: 15%
```

## 6. Integration Examples

### Shell script integration:
```bash
#!/bin/bash
# Generate secure password and save to clipboard
password=$(CipherSmith generate --no-color)
echo $password | clip
```

### Python integration:
```python
from CipherSmith import generate_password

# Generate password with custom rules
password = generate_password(
    length=16,
    uppercase=2,
    lowercase=8,
    digits=3,
    special=3
)
```

## Need Help?

- Run `CipherSmith --help` for command overview
- Run `CipherSmith COMMAND --help` for command-specific help
- Visit our [Documentation](https://CipherSmith.readthedocs.io/) for detailed guides
- Open an [Issue](https://github.com/Amul-Thantharate/CipherSmith/issues) for support
