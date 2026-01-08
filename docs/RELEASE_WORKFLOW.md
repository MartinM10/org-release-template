# Flujo de Releases Automáticas

Este documento explica cómo funcionan las releases automáticas con **release-please**.

## Visión General

```
Commits → main → Release Please → Release PR → Merge → GitHub Release + Tag
```

## Cómo Funciona

### 1. Desarrollo Normal

Los desarrolladores trabajan en sus ramas y crean PRs hacia `main`:

```
feature/login ─────► PR ─────► main
```

### 2. Merge a Main

Cuando un PR se mergea a `main`, **release-please** analiza los commits.

### 3. Release PR Automático

Si hay commits relevantes (`feat`, `fix`, etc.), release-please crea o actualiza un **Release PR**:

- 📝 Actualiza `CHANGELOG.md` automáticamente
- 🔢 Calcula la nueva versión según SemVer
- 📦 Actualiza `version` en `package.json`

### 4. Merge del Release PR

Cuando el equipo decide hacer una release, mergea el Release PR. Esto automáticamente:

- 🏷️ Crea un tag de versión (ej: `v1.2.0`)
- 📢 Crea un GitHub Release con notas
- ✅ Marca los issues relacionados (si aplica)

## Diagrama Detallado

```
┌──────────────────────────────────────────────────────────────────┐
│                       Desarrollo                                 │
└────────────────────────────┬─────────────────────────────────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
    ▼                        ▼                        ▼
┌─────────┐            ┌─────────┐            ┌─────────┐
│ feat:   │            │ fix:    │            │ docs:   │
│ login   │            │ bug #42 │            │ readme  │
└────┬────┘            └────┬────┘            └────┬────┘
     │                      │                      │
     └──────────────────────┼──────────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Merge a main │
                    └───────┬───────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │     release-please.yml      │
              │   analiza nuevos commits    │
              └─────────────┬───────────────┘
                            │
              ┌─────────────┴───────────────┐
              │                             │
              ▼                             ▼
    ┌─────────────────┐          ┌─────────────────┐
    │ Commits con     │          │ Solo docs/ci/   │
    │ feat/fix/perf   │          │ chore commits   │
    └────────┬────────┘          └────────┬────────┘
             │                            │
             ▼                            ▼
    ┌─────────────────┐          ┌─────────────────┐
    │ Crear/Actualizar│          │ No se crea      │
    │ Release PR      │          │ Release PR      │
    └────────┬────────┘          └─────────────────┘
             │
             ▼
    ┌─────────────────┐
    │ CHANGELOG.md    │
    │ actualizado     │
    │ automáticamente │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Equipo revisa   │
    │ y aprueba       │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Merge Release PR│
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ GitHub Actions  │
    │ crea:           │
    │ • Tag v1.2.0    │
    │ • GitHub Release│
    └─────────────────┘
```

## Versionado Semántico (SemVer)

release-please calcula la versión automáticamente:

| Tipo de Commit | Bump de Versión | Ejemplo |
|----------------|-----------------|---------|
| `fix:` | PATCH | 1.0.0 → 1.0.1 |
| `feat:` | MINOR | 1.0.0 → 1.1.0 |
| `BREAKING CHANGE` | MAJOR | 1.0.0 → 2.0.0 |

## Ejemplo de CHANGELOG Generado

```markdown
## [1.2.0](https://github.com/org/repo/compare/v1.1.0...v1.2.0) (2026-01-08)

### Features

* add user authentication ([#15](https://github.com/org/repo/issues/15))
* implement dark mode support ([#18](https://github.com/org/repo/issues/18))

### Bug Fixes

* resolve memory leak in dashboard ([#16](https://github.com/org/repo/issues/16))
* fix login button not responding ([#17](https://github.com/org/repo/issues/17))
```

## FAQ

### ¿Con qué frecuencia debo hacer releases?

- **Recomendado**: Cuando el Release PR acumule cambios significativos
- **Mínimo**: Al menos una vez por sprint/iteración
- **Máximo**: No dejes acumular demasiados cambios

### ¿Qué pasa si quiero saltarme un commit en la release?

Usa el tipo `chore:` o añade `skip-release` en el mensaje:

```bash
chore: update dependencies [skip-release]
```

### ¿Puedo hacer releases manuales?

Sí, pero no es recomendado. release-please maneja todo automáticamente.

### ¿Cómo hago un hotfix?

1. Crea un branch desde `main`
2. Haz el fix con `fix: descripción`
3. Crea PR a `main`
4. Mergea el PR
5. Mergea el Release PR que se genera

## Archivos Importantes

| Archivo | Propósito |
|---------|-----------|
| `.release-please-manifest.json` | Versión actual del proyecto |
| `.github/release-please-config.json` | Configuración del release |
| `CHANGELOG.md` | Historial de cambios (auto-generado) |

## Referencias

- [release-please GitHub](https://github.com/googleapis/release-please)
- [Semantic Versioning](https://semver.org/)
