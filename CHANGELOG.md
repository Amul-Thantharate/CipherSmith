# Changelog

All notable changes to securekey will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Project initialization and basic structure
- Command-line interface for password generation
- Password strength analysis feature
- Password history management
- Search functionality for stored passwords
- Statistics tracking for password generation
- Documentation improvements

### Changed
- Renamed project from secure-passgen-cli to securekey
- Updated all documentation to reflect new name
- Improved README with badges and detailed information

### Security
- Implemented secure random generation using secrets module
- Added encryption for stored passwords
- Implemented secure password deletion

## [0.1.0] - 2024-01-14

### Added
- Initial release
- Basic password generation functionality
- Command-line interface
- Support for customizable password length
- Special character inclusion/exclusion
- Number and uppercase letter options
- File saving capability
- Basic documentation

### Security
- Basic password generation security
- Local storage of passwords

[Unreleased]: https://github.com/Amul-Thantharate/securekey/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Amul-Thantharate/securekey/releases/tag/v0.1.0
