# CipherSmith Demo Guide

This guide demonstrates the key features of CipherSmith through practical examples.

## Basic Password Generation

Generate a simple password with default settings:
```bash
CipherSmith generate
```

Generate a password with specific length:
```bash
CipherSmith generate --total-length 16
```

Generate multiple passwords:
```bash
CipherSmith generate --amount 5
```

## Advanced Password Generation

Generate a password with specific character requirements:
```bash
CipherSmith generate --uppercase 2 --lowercase 6 --numbers 2 --special-chars 2
```

Generate a password with description and tags:
```bash
CipherSmith generate -t 16 -d "GitHub Account" --tag "work" --tag "github"
```

Exclude similar characters:
```bash
CipherSmith generate --exclude-similar
```

## Password Strength Analysis

Check strength of an existing password:
```bash
CipherSmith check "YourPassword123"
```

Get detailed strength analysis:
```bash
CipherSmith check "YourPassword123" --verbose
```

Sample output:
```
Password Strength Analysis:
Score: 3/4
Crack Time: 3 days
Feedback: Uses common patterns

Additional Details:
Length: 14
Patterns Found: dictionary_word, sequential_numbers
Suggestions: Add more unique characters, avoid common sequences
```

## Password History Management

View recent password history:
```bash
CipherSmith history
```

Search passwords by description or tags:
```bash
CipherSmith search "github"
```

View password generation statistics:
```bash
CipherSmith stats
```

Clear password history:
```bash
CipherSmith clear
```

Delete specific password entry:
```bash
CipherSmith delete [ID]
```

## Advanced Features

### Password Generation with All Options
```bash
CipherSmith generate \
    --total-length 20 \
    --uppercase 4 \
    --lowercase 8 \
    --numbers 4 \
    --special-chars 4 \
    --exclude-similar \
    --description "AWS Root Account" \
    --tag "cloud" \
    --tag "aws" \
    --tag "important"
```

### Strength Check with Verbose Output
```bash
CipherSmith check "MyC0mpl3x!P@ssw0rd" --verbose
```

Sample output:
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

## Tips and Best Practices

1. Always use the `--verbose` flag with the check command for detailed analysis
2. Tag passwords for better organization
3. Use descriptions to remember the purpose of each password
4. Regularly review password history for weak passwords
5. Use the statistics command to track password generation patterns

## Error Handling

CipherSmith provides clear error messages:

Invalid length:
```bash
CipherSmith generate --total-length 2
# Error: Password length must be at least 8 characters
```

Character requirements exceed length:
```bash
CipherSmith generate --total-length 10 --uppercase 6 --numbers 6
# Error: Sum of character requirements exceeds total length
```

## Database Operations

The password history is stored in a secure SQLite database with encryption. The database is automatically created in your user directory.

To manage the database:
- View history: `CipherSmith history`
- Clear all entries: `CipherSmith clear`
- Delete specific entry: `CipherSmith delete [ID]`
- Search entries: `CipherSmith search [QUERY]`

## Version Information

Check CipherSmith version:
```bash
CipherSmith --version
```

Get help:
```bash
CipherSmith --help
```

For command-specific help:
```bash
CipherSmith [COMMAND] --help
