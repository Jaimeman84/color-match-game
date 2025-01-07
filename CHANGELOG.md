# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-01-07

### Added
- Score tracking system
- Reset game button
- Color similarity detection
- Unit tests for all core functionality
- Development tools (black, isort, flake8, mypy)

### Changed
- Reorganized project structure using proper Python packaging
- Updated from experimental_rerun to rerun for Streamlit compatibility
- Improved state management for better game flow
- Separated configuration into config.py

### Fixed
- Double-click requirement for new round generation
- Color generation to ensure distinct options
- Import issues in test suite

## [1.0.0] - 2024-01-06

### Added
- Initial release
- Basic color matching gameplay
- Random color generation
- Simple UI with Streamlit
- Basic feedback system