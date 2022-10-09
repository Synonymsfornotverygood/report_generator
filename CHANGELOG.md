# Changelog

All notable changes to project will be documented in this file.

## [0.0.32] - 2022-10-09

Resolved bug with font selection in GUI referenced in Issue #4.

### Added

### Changed
- Changed the default config.yaml setup. The font settings options where all prefixed with the word 'default'. This has been removed from the config to match the expected font_options formatting. This may cause issues if the user updates their installation of package without updating config file.

### Fixed
- Fixed font selection in GUI window. Will now work without needing to click save settings first.