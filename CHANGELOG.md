# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0](https://github.com/MartinM10/org-release-template/compare/v1.1.0...v1.2.0) (2026-01-08)


### Added

* generalize template (remove code, add visual docs) ([31333e6](https://github.com/MartinM10/org-release-template/commit/31333e6bf23c6775dea98820dbd18233ed82f1e0))
* simplify template and add organization requirements ([c9ffef3](https://github.com/MartinM10/org-release-template/commit/c9ffef3890e1c11f5e92ba29791a44ac4a150058))


### Changed

* consolidate documentation and align with new python structure ([a5b1df5](https://github.com/MartinM10/org-release-template/commit/a5b1df56f9cd5a81d61ae788a14e5af2a3c22411))
* fix mermaid diagram on README.md ([d24789c](https://github.com/MartinM10/org-release-template/commit/d24789c2da905f7d4b004e699df4f3d67a65b971))
* fix mermaid diagram on README.md ([5f094ee](https://github.com/MartinM10/org-release-template/commit/5f094ee170934607de55911c292a0d4d768e6cc9))
* fixed mermaid diagram ([f30300f](https://github.com/MartinM10/org-release-template/commit/f30300fc368303843a4e1b95c9c12c40354e00f1))
* fixed mermaid diagram ([2588b73](https://github.com/MartinM10/org-release-template/commit/2588b7338a9784b2def8d5bc0ac63524076f488c))
* rename architecture template and emphasize conventional commits ([4c9316b](https://github.com/MartinM10/org-release-template/commit/4c9316bc618e49eb01e39c9ba8852335ba8b5a09))
* use mermaid for branch protection flow ([c60a782](https://github.com/MartinM10/org-release-template/commit/c60a78209656fbbf6f48c25f9de994fc8b31f873))

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
