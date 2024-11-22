# Changelog

All notable changes to CipherSmith will be documented in this file.

## [1.3.0] - 2024-03-20

### Added
- New history command with improved formatting using rich tables
- Enhanced password history display with timestamp, ID, and tags
- Support for filtering history by tags
- Limit option for controlling the number of history entries displayed
- Improved error handling in history retrieval
- Better datetime formatting in history display

### Changed
- Refactored password history database implementation
- Enhanced database schema for better history tracking
- Improved command-line interface for history command
- Updated error messages with more detailed feedback
- Better handling of JSON fields in database

### Fixed
- History command error handling and display issues
- Database connection management
- JSON parsing for tags and configuration
- Datetime parsing and display formatting
- Exit code handling for better error reporting

## [1.2.0] - 2024-03-19

### Added
- Enhanced password strength analysis with detailed feedback using zxcvbn
- Comprehensive documentation (INSTALL.md, DEMO.md)
- GitHub Actions workflow for automated testing and releases
- PyPI publishing configuration
- Verbose mode for password strength checker
- Improved error handling in CLI commands
- Cross-platform compatibility improvements
- Package distribution files (wheel and source)

### Changed
- Updated password validation logic with enhanced security
- Improved command-line interface with rich formatting
- Enhanced error messages and user feedback
- Refactored database access for better reliability
- Updated dependencies to latest stable versions
- Streamlined installation process
- Enhanced package structure and organization

### Fixed
- Module import issues resolved
- Password strength analysis display improvements
- Package installation and dependency handling
- Cross-platform compatibility issues
- Documentation formatting and clarity

### Security
- Implemented secure password storage mechanisms
- Enhanced encryption for sensitive data
- Added comprehensive password strength indicators
- Improved security best practices documentation

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
