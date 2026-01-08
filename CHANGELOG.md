# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Migrate template from JavaScript to Python
- Add `pyproject.toml` for Python project configuration
- Add `ruff` as linter and formatter
- Add `pre-commit` hooks for commit validation

### Changed

- Replace `npm`/`eslint` with `pip`/`ruff`
- Replace `husky` with `pre-commit`
- Update CI workflow for Python
- Configure CHANGELOG format to follow Keep a Changelog standard

### Removed

- Remove JavaScript files (`package.json`, `eslint.config.js`, etc.)
- Remove Node.js dependencies

---

## [1.1.0] - 2026-01-08

### Added

- Math utility functions (`multiply`, `divide`, `formatVersion`)

## [1.0.0] - 2026-01-08

### Added

- Initial template setup with CI/CD and conventional commits

### Fixed

- Add explicit token to release-please workflow
- Simplify release-please configuration

[Unreleased]: https://github.com/MartinM10/org-release-template/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/MartinM10/org-release-template/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/MartinM10/org-release-template/releases/tag/v1.0.0
