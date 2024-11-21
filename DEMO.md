# Secure Password Generator CLI - Demo Guide

This guide demonstrates the various features and use cases of the Secure Password Generator CLI tool.

## Basic Password Generation

1. Generate a default password (12 characters):
```bash
passforge generate
# Output: Kj9$mP2#nL5q
```

2. Generate a password with specific length:
```bash
passforge generate -t 16
# Output: P@5kL8#mN9$vB2xQ
```

3. Generate multiple passwords:
```bash
passforge generate -a 3
# Output:
# Rj7#kP9$mN2q
# Ht5$vB8#nL4w
# Qs3#mK7$pJ9x
```

## Advanced Password Generation

1. Control character composition:
```bash
# 2 numbers, 3 lowercase, 4 uppercase, 1 special
passforge generate -n 2 -l 3 -u 4 -s 1
# Output: NK2cat3L#P
```

2. Exclude similar characters:
```bash
passforge generate -t 12 -e
# Output: (excludes O, 0, I, l, etc.)
```

3. Generate without special characters:
```bash
passforge generate --no-specials
# Output: Kj9mP2nL5qBv
```

## Password Organization

1. Add description and tags:
```bash
passforge generate -t 16 -d "GitHub Account" --tag github --tag work
# Output: 2Y@y^A6t|KPQ)-/3
# Saved with description and tags
```

2. Save multiple passwords to file:
```bash
passforge generate -a 3 -o passwords.txt
# Creates passwords.txt with 3 passwords
```

## Password History Management

1. View recent password history:
```bash
passforge history
# Shows table with recent passwords
```

2. Filter history by tag:
```bash
passforge history --tag work
# Shows passwords tagged with 'work'
```

3. Search passwords:
```bash
# Search by description
passforge search "github"
# Shows passwords with 'github' in description or tags

# Search with limit
passforge search "work" --limit 5
# Shows up to 5 matching passwords
```

4. View statistics:
```bash
passforge stats
# Shows password generation statistics
```

5. Clear old passwords:
```bash
# Clear passwords older than 30 days
passforge clear --days 30
```

## Best Practices

1. Use descriptive tags for better organization:
```bash
passforge generate -d "Work Email" --tag email --tag work --tag important
```

2. Regular password rotation:
```bash
# Generate and tag as replacement
passforge generate -t 16 -d "GitHub (New)" --tag github --tag rotation
```

3. Search and verify before clearing:
```bash
# Check old passwords
passforge search "old"
# Clear if needed
passforge clear --days 90
```

## Security Tips

1. Use sufficient length (16+ characters for critical accounts):
```bash
passforge generate -t 20 -d "Banking Account" --tag financial
```

2. Include all character types for maximum security:
```bash
passforge generate -n 4 -l 4 -u 4 -s 4 -d "Critical System" --tag secure
```

3. Regular backups:
```bash
# Export recent passwords to file
passforge history --limit 100 > password_backup.txt
```

## Advanced Search Examples

1. Search by multiple criteria:
```bash
# Find work-related email passwords
passforge search "email" --tag work
```

2. Case-insensitive search:
```bash
# These searches are equivalent
passforge search "GitHub"
passforge search "github"
```

3. Search with context:
```bash
# Find recently rotated passwords
passforge search "rotation" --limit 5
```

## Comprehensive Examples and Best Practices

### 1. Generate Simple Password
```bash
# Generate a default 12-character password
passforge generate
> Kj9#mP2$nL5@

# Generate a longer 16-character password
passforge generate -t 16
> Hy7#kL9$mN4@pQ2&
```

### 2. Generate Multiple Passwords
```bash
# Generate 3 passwords
passforge generate -a 3
> Kj9#mP2$nL5@
> Qw5&xY8*vM3!
> Zt4@hN7$bK9#

# Generate 5 passwords of length 8
passforge generate -t 8 -a 5
> Kj9#mP2$
> Qw5&xY8*
> Zt4@hN7$
> Bv6#cL4*
> Hy3$pW9@
```

### 3. Password with Specific Composition
```bash
# Generate password with:
# - 2 numbers
# - 3 lowercase letters
# - 4 uppercase letters
# - 1 special character
passforge generate -n 2 -l 3 -u 4 -s 1
> 12abcDEFG#

# Exclude similar characters (0, O, 1, l, etc.)
passforge generate --no-similar
> Kj9#mP2$nL5@
```

### 4. Using Tags and Descriptions

#### 1. Generate Password with Description
```bash
# Add a description
passforge generate -d "GitHub Account"
> Kj9#mP2$nL5@

# Add description and tags
passforge generate -d "Work Email" --tag email --tag work
> Qw5&xY8*vM3!
```

#### 2. Generate Multiple Passwords with Tags
```bash
# Generate 3 passwords for social media accounts
passforge generate -a 3 -d "Social Media Accounts" --tag social --tag personal
> Kj9#mP2$nL5@
> Qw5&xY8*vM3!
> Zt4@hN7$bK9#
```

### 5. Search and History Management

#### 1. View Password History
```bash
# View recent history
passforge history

# View last 20 entries
passforge history --limit 20

# Filter by tag
passforge history --tag work
```

#### 2. Search Passwords
```bash
# Search by description
passforge search "github"

# Search with tag
passforge search "email" --limit 5

# Search across all fields
passforge search "work"
```

#### 3. Delete Password Entries
```bash
# Delete with confirmation
passforge delete 123

# Force delete without confirmation
passforge delete 456 --force
```

### 6. Statistics and Analysis

```bash
# View overall statistics
passforge stats

# Sample output:
Password Generation Statistics
Total Passwords Generated: 50
Average Password Length: 12.8
Most Used Tags:
  work: 15
  personal: 12
  social: 8
Recent Daily Generation:
  2024-11-20: 10 passwords
```

### 7. Security Best Practices

1. **Password Length**
   - Use at least 12 characters for regular accounts
   - Use 16+ characters for critical accounts
   - Example: `passforge generate -t 16`

2. **Character Composition**
   - Include all character types for maximum security
   - Example: `passforge generate -n 3 -l 4 -u 4 -s 2`

3. **Password Storage**
   - Always add descriptions for context
   - Use meaningful tags for organization
   - Example: `passforge generate -d "Bank Account" --tag financial --tag critical`

4. **Regular Rotation**
   - Generate new passwords periodically
   - Delete old unused passwords
   - Example: `passforge delete <id>` for old entries

### 8. Advanced Usage Tips

1. **Organizing with Tags**
   - Use consistent tag naming
   - Combine multiple tags for better organization
   - Example: `--tag work --tag email --tag critical`

2. **Efficient Searching**
   - Use specific search terms
   - Combine with limit for faster results
   - Example: `passforge search "bank" --limit 5`

3. **Batch Operations**
   - Generate multiple passwords at once
   - Use consistent descriptions
   - Example: `passforge generate -a 3 -d "Social Media" --tag social`

4. **History Management**
   - Regularly review password history
   - Delete unnecessary entries
   - Keep descriptions updated

Remember to store your generated passwords securely and never share them. The tool's history feature is designed for reference only and stores hashed versions of the passwords for security.

# PassForge Demo Guide

This guide demonstrates the various features and capabilities of PassForge, a powerful command-line password generator.

## Basic Usage

### Generate a Simple Password
Generate a password with default settings (16 characters, including uppercase, lowercase, numbers, and special characters):

```bash
$ passforge generate
Generated password: Kj#9mP$vL2nX&qR5
```

### Specify Password Length
Create a password with a custom length:

```bash
$ passforge generate --length 12
Generated password: Nh#7kL$pM2nX
```

## Advanced Features

### Customize Character Sets

Generate a password with specific character types:

```bash
# Only lowercase and numbers
$ passforge generate --lowercase --numbers --length 10
Generated password: a7n9k2m4p6

# Include special characters
$ passforge generate --special-chars --length 14
Generated password: P#k9$mN&v2@xL4

# Exclude ambiguous characters
$ passforge generate --no-ambiguous --length 12
Generated password: Kp9mNv2xL4Rj
```

### Generate Multiple Passwords

Create multiple passwords at once:

```bash
$ passforge generate --count 3 --length 10
Generated passwords:
1. Kj#9mP$vL2
2. Nh#7kL$pM2
3. Qw#5jR$tN8
```

### Save to File

Save generated passwords to a file:

```bash
$ passforge generate --save passwords.txt --count 3
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
$ passforge generate --min-special 2 --min-numbers 2 --min-uppercase 2
Generated password: Kj#9mP$vL2nX&qR5

# Generate memorable passwords
$ passforge generate --memorable
Generated password: CorrectHorseBatteryStaple
```

### Check Password Strength

Analyze the strength of a password:

```bash
$ passforge check "MyPassword123"
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
        ["passforge", "generate", "--length", "16"],
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
$ passforge batch --services "github,gmail,gitlab" --prefix "dev-"
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
$ passforge: command not found
```
Solution: Ensure PassForge is installed correctly:
```bash
$ pip install --user passforge
```

### Issue: Permission Denied
```bash
$ passforge generate --save /root/passwords.txt
Permission denied
```
Solution: Use a path where you have write permissions:
```bash
$ passforge generate --save ~/passwords.txt
```

## Additional Resources

- GitHub repository: [https://github.com/Amul-Thantharate/passforge](https://github.com/Amul-Thantharate/passforge)
- Bug reports: [https://github.com/Amul-Thantharate/passforge/issues](https://github.com/Amul-Thantharate/passforge/issues)

For more information and updates, visit our GitHub repository or read the full documentation.
