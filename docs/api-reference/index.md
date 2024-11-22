---
layout: default
title: API Reference
permalink: /CipherSmith/api-reference/
---

# 📚 CipherSmith API Reference

## 🔧 Core Components

### PasswordDatabase

The main database interface for password management.

#### Methods

##### `__init__(db_path: Optional[str] = None)`
Initialize database connection.
- `db_path`: Optional path to database file. Defaults to user's home directory.

##### `add_password(password_hash: str, length: int, config: Dict[str, Any], description: Optional[str] = None, tags: Optional[List[str]] = None) -> int`
Add a password to history.
- Returns: ID of the new entry

##### `get_password_history(limit: Optional[int] = None, tag: Optional[str] = None) -> List[Dict[str, Any]]`
Retrieve password history.
- `limit`: Maximum number of entries
- `tag`: Filter by tag
- Returns: List of password entries

##### `get_all_tags() -> List[str]`
Get all unique tags.
- Returns: List of tag strings

##### `search_passwords(query: str) -> List[Dict[str, Any]]`
Search password history.
- `query`: Search term
- Returns: Matching password entries

##### `delete_password(entry_id: int) -> bool`
Delete a password entry.
- Returns: Success status

##### `clear_history(days: Optional[int] = None)`
Clear password history.
- `days`: Optional age limit in days

### PasswordStrengthAnalyzer

Password strength analysis functionality.

#### Methods

##### `analyze_password(password: str, verbose: bool = False) -> Dict[str, Any]`
Analyze password strength.
- Returns: Analysis results

## 🎯 CLI Commands

### generate

```python
@app.command()
def generate(
    total_length: int = None,
    exclude_similar: bool = False,
    amount: int = 1,
    numbers: int = 0,
    lowercase: int = 0,
    uppercase: int = 0,
    special_chars: int = 0,
    no_specials: bool = False,
    output_file: Path = None,
    description: str = None,
    tags: List[str] = None,
    verbose: bool = False,
    save_history: bool = True,
    check_strength: bool = False,
)
```

Generate secure passwords with customizable options.

### check

```python
@app.command()
def check(
    password: str,
    verbose: bool = False,
)
```

Analyze password strength with detailed feedback.

### history

```python
@app.command()
def history(
    limit: int = 10,
    tag: str = None,
)
```

View password generation history.

### search

```python
@app.command()
def search(
    query: str,
    limit: int = 10,
)
```

Search password history.

### clear

```python
@app.command()
def clear(
    days: int = None,
    force: bool = False,
)
```

Clear password history.

## 📊 Data Structures

### Password Entry
```python
{
    'id': int,
    'password_hash': str,
    'created_at': str,
    'length': int,
    'config': Dict[str, Any],
    'description': Optional[str],
    'tags': Optional[List[str]]
}
```

### Password Analysis Result
```python
{
    'score': int,
    'feedback': Dict[str, str],
    'crack_times': Dict[str, float],
    'patterns': List[Dict[str, Any]]
}
```

## 🔒 Security Considerations

### Password Storage
- Passwords are hashed before storage
- SQLite database is used with proper indexing
- Database file permissions are restricted

### Random Generation
- Uses `secrets` module for cryptographic security
- Implements entropy pooling for better randomness
- Avoids predictable patterns

### Error Handling
- Secure error messages
- No sensitive data in logs
- Proper resource cleanup

## 🔧 Configuration

### Database Location
- Default: `~/.secure_passgen/passwords.db`
- Configurable via environment variables
- Supports custom paths

### Character Sets
```python
NUMBERS = string.digits
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
```

## 📈 Performance Considerations

### Database Operations
- Uses connection pooling
- Implements proper indexing
- Batch operations for efficiency

### Memory Usage
- Streaming large results
- Proper resource cleanup
- Efficient data structures

## 🐛 Error Codes

- `0`: Success
- `1`: General error
- `2`: Database error
- `3`: Invalid input
- `4`: Permission error
