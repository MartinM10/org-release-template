# Conventional Commits - Guía Rápida

Esta guía explica el formato de commits que usamos en la organización.

## ¿Por qué Conventional Commits?

- 📖 Historial de commits legible
- 🤖 Generación automática de CHANGELOG
- 🔢 Versionado semántico automático
- 👥 Comunicación clara entre equipos

## Formato

```
<tipo>[ámbito opcional]: <descripción>

[cuerpo opcional]

[footer(s) opcional]
```

## Tipos de Commits y Mapeo a CHANGELOG

Usamos el estándar [Keep a Changelog](https://keepachangelog.com/) para el CHANGELOG:

| Tipo | Sección CHANGELOG | Bump SemVer | Descripción |
|------|-------------------|-------------|-------------|
| `feat` | **Added** | MINOR (0.X.0) | Nueva funcionalidad |
| `fix` | **Fixed** | PATCH (0.0.X) | Corrección de bug |
| `perf` | **Changed** | PATCH | Mejora de rendimiento |
| `refactor` | **Changed** | - | Cambio de código sin feat ni fix |
| `docs` | **Changed** | - | Solo documentación |
| `style` | (oculto) | - | Formato (espacios, comas, etc.) |
| `test` | (oculto) | - | Añadir o corregir tests |
| `build` | (oculto) | - | Cambios en build o dependencias |
| `ci` | (oculto) | - | Cambios en CI/CD |
| `chore` | (oculto) | - | Tareas de mantenimiento |
| `revert` | **Changed** | - | Revierte un commit anterior |
| `BREAKING CHANGE` | **⚠ BREAKING** | MAJOR (X.0.0) | Cambio incompatible |

## Ejemplos

### ✅ Commits Correctos

```bash
# Nueva funcionalidad → Sección "Added"
feat: add user authentication system

# Corrección de bug → Sección "Fixed"
fix: resolve login timeout issue

# Con ámbito
feat(api): add pagination to users endpoint

# Con cuerpo explicativo
fix: prevent race condition in data sync

Multiple users reported data loss when syncing simultaneously.
This fix adds a mutex lock to prevent concurrent writes.

# Breaking change → Sección "BREAKING CHANGES"
feat!: remove deprecated API endpoints

BREAKING CHANGE: The /v1/users endpoint has been removed.
Use /v2/users instead.
```

### ❌ Commits Incorrectos

```bash
# Sin tipo
added new feature

# Tipo en mayúsculas
FEAT: add login

# Descripción muy larga (usa el cuerpo)
feat: add user authentication system with JWT tokens and refresh token rotation including password reset functionality
```

## Resultado en CHANGELOG

Cuando usas los tipos correctamente, el CHANGELOG se genera así:

```markdown
## [1.2.0] - 2026-01-15

### Added
- Add user authentication system (#15)
- Implement dark mode support (#18)

### Fixed
- Resolve memory leak in dashboard (#16)
- Fix login button not responding (#17)

### Changed
- Improve database query performance (#20)
```

## Tips

1. **Descripción clara** - Describe qué hace el cambio
2. **Sin punto final** - No termines la descripción con punto
3. **Modo imperativo** - "add feature" no "added feature"
4. **Sé específico** - "fix login button" mejor que "fix bug"
5. **Un cambio por commit** - Facilita el rollback

## Validación Local

El proyecto usa `pre-commit` con `conventional-pre-commit` para validar commits:

```bash
# Instalar hooks
pre-commit install
pre-commit install --hook-type commit-msg
```

Si tu commit es rechazado, verás un error indicando el problema.

## Títulos de Pull Request

Los títulos de PR **también deben seguir este formato**, ya que se usan para generar el CHANGELOG.

```
feat: add dark mode support
fix: resolve memory leak in dashboard
docs: update API documentation
```

## Referencias

- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
