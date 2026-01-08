# 🚀 Organization Release Template

Template repository con CI/CD completo, Conventional Commits y releases automáticas para la organización.

## ✨ Características

- 🔄 **CI/CD con GitHub Actions** - Lint, test automáticos
- 📝 **Conventional Commits** - Formato estándar de commits
- 🏷️ **Releases automáticas** - Con release-please de Google
- 📋 **CHANGELOG automático** - Formato [Keep a Changelog](https://keepachangelog.com/)
- 🔒 **Protección de ramas** - Guía incluida

## 📁 Estructura

```
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # CI: lint, test
│   │   ├── release-please.yml
│   │   └── pr-check.yml
│   ├── release-please-config.json
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                       # Documentación
│   ├── BRANCH_PROTECTION.md
│   ├── CONVENTIONAL_COMMITS.md
│   └── RELEASE_WORKFLOW.md
├── src/                        # Código fuente
│   └── utils.py
├── tests/                      # Tests
├── .pre-commit-config.yaml     # Pre-commit hooks
├── pyproject.toml              # Config del proyecto
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

## 🚦 Inicio Rápido

### 1. Usar este Template

Haz clic en **"Use this template"** → **"Create a new repository"**

### 2. Clonar e Instalar

```bash
git clone https://github.com/tu-org/tu-repo.git
cd tu-repo

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -e ".[dev]"

# Instalar pre-commit hooks
pre-commit install
pre-commit install --hook-type commit-msg
```

### 3. Proteger la Rama Main

Sigue la guía en [docs/BRANCH_PROTECTION.md](docs/BRANCH_PROTECTION.md)

### 4. ¡Empieza a Desarrollar!

```bash
# Crear branch
git checkout -b feature/mi-feature

# Hacer cambios y commit (formato convencional)
git commit -m "feat: add awesome feature"

# Crear PR
git push origin feature/mi-feature
```

## 📖 Documentación

| Documento | Descripción |
|-----------|-------------|
| [CONTRIBUTING.md](CONTRIBUTING.md) | Guía de contribución |
| [Conventional Commits](docs/CONVENTIONAL_COMMITS.md) | Formato de commits |
| [Branch Protection](docs/BRANCH_PROTECTION.md) | Cómo proteger main |
| [Release Workflow](docs/RELEASE_WORKFLOW.md) | Flujo de releases |

## 🔧 Comandos Útiles

```bash
# Lint
ruff check src/

# Formatear
ruff format src/

# Tests
pytest tests/ -v

# Pre-commit en todos los archivos
pre-commit run --all-files
```

## 📋 Flujo de Trabajo

```
1. Crea branch desde main
2. Haz commits con formato convencional
3. Crea PR → CI corre automáticamente
4. Obtén aprobación → Merge
5. release-please crea Release PR
6. Merge Release PR → Nueva versión publicada
```

## 🏷️ Versionado

Usamos [SemVer](https://semver.org/) con formato [Keep a Changelog](https://keepachangelog.com/):

| Tipo de Commit | Sección CHANGELOG | Versión |
|----------------|-------------------|---------|
| `feat:` | **Added** | MINOR (0.X.0) |
| `fix:` | **Fixed** | PATCH (0.0.X) |
| `refactor:`, `perf:` | **Changed** | - |
| `BREAKING CHANGE` | **⚠ BREAKING** | MAJOR (X.0.0) |

## 📄 Licencia

[MIT](LICENSE)
