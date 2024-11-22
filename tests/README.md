# CipherSmith Test Suite

This directory contains comprehensive tests for the CipherSmith password manager. The test suite ensures the reliability and security of all major components.

## Test Structure

- `test_password_generator.py`: Tests for password generation functionality
- `test_encryption.py`: Tests for encryption and decryption operations
- `test_storage.py`: Tests for password storage and retrieval
- `test_cli.py`: Tests for command-line interface

## Running Tests

To run all tests:
```bash
python -m unittest discover tests
```

To run a specific test file:
```bash
python -m unittest tests/test_password_generator.py
```

To run a specific test case:
```bash
python -m unittest tests.test_password_generator.TestPasswordGenerator
```

## Test Coverage

The test suite covers:
- Password generation with various configurations
- Encryption/decryption of passwords and data
- Password storage operations (add, update, delete)
- Database import/export functionality
- CLI commands and interactions
- Error handling and edge cases

## Requirements

Required packages for running tests:
- unittest (built-in)
- cryptography
- mock (for CLI tests)

## Contributing

When adding new features to CipherSmith:
1. Add corresponding tests in the appropriate test file
2. Ensure all tests pass before submitting changes
3. Maintain test coverage above 80%
4. Follow the existing test structure and naming conventions

## Test Examples

### Password Generator Tests
```python
def test_generate_password_default(self):
    password = self.generator.generate()
    self.assertEqual(len(password), 12)  # Default length
    self.assertTrue(any(c.isupper() for c in password))
    self.assertTrue(any(c.islower() for c in password))
    self.assertTrue(any(c.isdigit() for c in password))
```

### Encryption Tests
```python
def test_encryption_decryption(self):
    original_data = "sensitive_password123"
    encrypted = self.encryptor.encrypt(original_data)
    decrypted = self.encryptor.decrypt(encrypted)
    self.assertEqual(decrypted, original_data)
```

### Storage Tests
```python
def test_add_password(self):
    service = "test_service"
    entry = {
        "username": "testuser",
        "password": "password123"
    }
    self.storage.add_password(service, **entry)
    stored = self.storage.get_password(service)
    self.assertEqual(stored["password"], entry["password"])
```

## Continuous Integration

The test suite is integrated with GitHub Actions and runs automatically on:
- Every push to main branch
- Pull request creation/updates
- Daily scheduled runs

## Security Notes

- Test files do not contain actual sensitive data
- Encryption tests use temporary keys
- All test files are cleaned up after execution
- Mock objects are used for sensitive operations
