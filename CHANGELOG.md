# Changelog

All notable changes to CipherSmith will be documented in this file.

## [1.2.0] - 2024-03-19

### Added
- Enhanced password strength analysis with detailed feedback
- Verbose mode for password strength checker
- Improved error handling in CLI commands
- Fixed import structure for better package stability

### Changed
- Updated password validation logic
- Improved command-line interface feedback
- Enhanced error messages and user feedback
- Refactored database access for better reliability

### Fixed
- Module import issues
- Password strength analysis display
- Database initialization in test environments
- Command visibility in CLI help

## [1.1.0] - 2024-01-20

### Added
- Real-time password strength visualization
- Advanced password analysis using zxcvbn
- New `check` command for analyzing password strength
- Password pattern detection and feedback
- Estimated crack time calculation
- Rich terminal visualization
- `--check-strength` flag for generate command

### Changed
- Enhanced password generation feedback
- Improved CLI output formatting
- Updated dependencies for better security analysis
- Modernized terminal output with rich progress bars

### Security
- Added comprehensive password strength analysis
- Enhanced pattern detection for common vulnerabilities
- Real-time feedback on password security

## [1.0.0] - 2024-01-15

### Added
- Initial release
- Basic password generation
- Customizable password rules
- Password history tracking
- Search and tag functionality
- Basic statistics
- SQLite database storage
