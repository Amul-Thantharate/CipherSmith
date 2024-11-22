# CipherSmith 1.3.0 Release

We're excited to announce CipherSmith 1.3.0! This release brings significant improvements to password history management and user experience.

## 🌟 Highlights

- **Enhanced History Command**: New and improved history command with rich table formatting
- **Better History Management**: Advanced filtering and display options for password history
- **Improved Error Handling**: More robust error handling and user feedback

## 🚀 New Features

### History Command Enhancements
- Beautiful rich table display for password history
- Filter history entries by tags
- Limit the number of displayed entries
- Improved timestamp formatting
- Better organization of history data

### Database Improvements
- Enhanced schema for better history tracking
- Improved JSON field handling
- Better connection management

### User Experience
- More detailed error messages
- Better feedback for command execution
- Improved datetime display formatting

## 🔧 Technical Improvements

- Refactored database implementation
- Enhanced error handling
- Improved JSON parsing
- Better exit code handling
- Updated documentation

## 📦 Installation

```bash
pip install CipherSmith==1.3.0
```

## 🔍 Usage

View password history:
```bash
CipherSmith history
```

Filter by tag:
```bash
CipherSmith history --tag work
```

Limit entries:
```bash
CipherSmith history --limit 5
```

## 🔗 Links

- [Documentation](https://github.com/amulthantharate/CipherSmith/blob/main/README.md)
- [Changelog](https://github.com/amulthantharate/CipherSmith/blob/main/CHANGELOG.md)
- [PyPI Package](https://pypi.org/project/CipherSmith/)
