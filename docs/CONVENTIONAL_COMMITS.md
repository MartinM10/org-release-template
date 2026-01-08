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

## Tipos de Commits

| Tipo | Descripción | Bump SemVer |
|------|-------------|-------------|
| `feat` | Nueva funcionalidad | MINOR (0.X.0) |
| `fix` | Corrección de bug | PATCH (0.0.X) |
| `docs` | Solo documentación | - |
| `style` | Formato (espacios, comas, etc.) | - |
| `refactor` | Cambio de código sin feat ni fix | - |
| `perf` | Mejora de rendimiento | PATCH |
| `test` | Añadir o corregir tests | - |
| `build` | Cambios en build o dependencias | - |
| `ci` | Cambios en CI/CD | - |
| `chore` | Tareas de mantenimiento | - |
| `revert` | Revierte un commit anterior | - |

## Ejemplos

### ✅ Commits Correctos

```bash
# Nueva funcionalidad
feat: add user authentication system

# Corrección de bug
fix: resolve login timeout issue

# Con ámbito
feat(api): add pagination to users endpoint

# Con cuerpo explicativo
fix: prevent race condition in data sync

Multiple users reported data loss when syncing simultaneously.
This fix adds a mutex lock to prevent concurrent writes.

# Breaking change
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

# Descripción en mayúsculas
feat: Add Login Feature

# Descripción muy larga (usa el cuerpo)
feat: add user authentication system with JWT tokens and refresh token rotation including password reset functionality
```

## Breaking Changes

Para indicar un cambio incompatible (MAJOR):

```bash
# Opción 1: Usar "!" después del tipo
feat!: change authentication flow

# Opción 2: Usar footer
feat: change authentication flow

BREAKING CHANGE: API tokens now expire after 24 hours.
```

## Tips

1. **Descripción en minúsculas** - Empieza siempre en minúscula
2. **Sin punto final** - No termines la descripción con punto
3. **Modo imperativo** - "add feature" no "added feature"
4. **Sé específico** - "fix login button" mejor que "fix bug"
5. **Un cambio por commit** - Facilita el rollback

## Validación Local

El proyecto usa `commitlint` + `husky` para validar commits localmente.

Si tu commit es rechazado, verás un error como:

```
⧗   input: Added new feature
✖   subject may not be empty [subject-empty]
✖   type may not be empty [type-empty]
```

## Títulos de Pull Request

Los títulos de PR **también deben seguir este formato**, ya que se usan para generar el CHANGELOG.

```
feat: add dark mode support
fix: resolve memory leak in dashboard
docs: update API documentation
```

## Referencias

- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
