# CipherSmith Demo Guide

This guide demonstrates the various features and capabilities of CipherSmith, a powerful command-line password generator.

## Basic Usage

### Generate a Simple Password
Generate a password with default settings (16 characters, including uppercase, lowercase, numbers, and special characters):

```bash
$ CipherSmith generate
Generated password: Kj#9mP$vL2nX&qR5
```

### Specify Password Length
Create a password with a custom length:

```bash
$ CipherSmith generate --length 12
Generated password: Nh#7kL$pM2nX
```

## Advanced Features

### Customize Character Sets

Generate a password with specific character types:

```bash
# Only lowercase and numbers
$ CipherSmith generate --lowercase --numbers --length 10
Generated password: a7n9k2m4p6

# Include special characters
$ CipherSmith generate --special-chars --length 14
Generated password: P#k9$mN&v2@xL4

# Exclude ambiguous characters
$ CipherSmith generate --no-ambiguous --length 12
Generated password: Kp9mNv2xL4Rj
```

### Generate Multiple Passwords

Create multiple passwords at once:

```bash
$ CipherSmith generate --count 3 --length 10
Generated passwords:
1. Kj#9mP$vL2
2. Nh#7kL$pM2
3. Qw#5jR$tN8
```

### Save to File

Save generated passwords to a file:

```bash
$ CipherSmith generate --save passwords.txt --count 3
Passwords saved to passwords.txt:
1. Kj#9mP$vL2nX&qR5
2. Nh#7kL$pM2nX@wS4
3. Qw#5jR$tN8bV%mK3
```

## Password Strength Features

### Generate Strong Passwords

Create passwords that meet specific strength requirements:

```bash
# Ensure minimum complexity
$ CipherSmith generate --min-special 2 --min-numbers 2 --min-uppercase 2
Generated password: Kj#9mP$vL2nX&qR5

# Generate memorable passwords
$ CipherSmith generate --memorable
Generated password: CorrectHorseBatteryStaple
```

### Check Password Strength

Analyze the strength of a password:

```bash
$ CipherSmith check "MyPassword123"
Password Strength Analysis:
- Length: Good (12 characters)
- Complexity: Medium
- Time to crack: ~3 days
Recommendation: Add special characters to increase strength
```

## Integration Examples

### Use in Scripts

Python script example:

```python
import subprocess

def generate_password():
    result = subprocess.run(
        ["CipherSmith", "generate", "--length", "16"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

password = generate_password()
print(f"Generated password: {password}")
```

### Batch Processing

Generate passwords for multiple services:

```bash
$ CipherSmith batch --services "github,gmail,gitlab" --prefix "dev-"
Generated passwords:
github: dev-Kj#9mP$vL2nX&qR5
gmail: dev-Nh#7kL$pM2nX@wS4
gitlab: dev-Qw#5jR$tN8bV%mK3
```

## Tips and Best Practices

1. Always use sufficient length (minimum 12 characters recommended)
2. Include a mix of character types for stronger passwords
3. Use the `--memorable` flag for passwords you need to remember
4. Save passwords securely using the `--save` option with encryption
5. Use the strength checker to validate password security

## Common Issues and Solutions

### Issue: Command Not Found
```bash
$ CipherSmith: command not found
```
Solution: Ensure CipherSmith is installed correctly:
```bash
$ pip install --user CipherSmith
```

### Issue: Permission Denied
```bash
$ CipherSmith generate --save /root/passwords.txt
Permission denied
```
Solution: Use a path where you have write permissions:
```bash
$ CipherSmith generate --save ~/passwords.txt
```

## Additional Resources

- GitHub repository: [https://github.com/Amul-Thantharate/CipherSmith](https://github.com/Amul-Thantharate/CipherSmith)
- Bug reports: [https://github.com/Amul-Thantharate/CipherSmith/issues](https://github.com/Amul-Thantharate/CipherSmith/issues)

For more information and updates, visit our GitHub repository or read the full documentation.
