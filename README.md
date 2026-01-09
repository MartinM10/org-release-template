# 📘 Guía de Referencia de Proyectos (Template)

Este repositorio sirve como **guía de referencia** estandarizada para proyectos de KHAOS / SEDIA.

## 📂 Estructura del Repositorio

Esta guía propone una **estructura flexible** para el código fuente, adaptada al lenguaje o framework que utilices.

Sin embargo, hay ciertos archivos estándar (como la configuración de release) que deben mantenerse.

A continuación se muestra un ejemplo de estructura mínima esperada:

```text
.
├── .github/
│   ├── workflows/
│   │   └── release-please.yml         # 🤖 Workflow de Release (Requerido)
│   └── release-please-config.json     # ⚙️ Configuración de Release (Requerido)
├── docs/
│   ├── assets/                # 📸 Imágenes, logos, diagramas
│   └── ARCHITECTURE.md        # 🏛️ Documentación de Arquitectura (Requerido)
├── src/                               # 📦 Tu código fuente (Nombre carpeta libre)
├── tests/                             # 🧪 Tus tests (Nombre carpeta libre)
├── .gitignore
├── CHANGELOG.md                       # 📝 Generado automáticamente
└── README.md
```

> [!NOTE]
> Los archivos que ves en la carpeta `docs/` de este repositorio (ej: `ORGANIZATION_REQUIREMENTS.md`, `BRANCH_PROTECTION.md`, `RELEASE_WORKFLOW.md`) son **documentación de esta guía**.
>
> **NO** es necesario copiarlos a tu repositorio. En tu proyecto, `docs/` debe contener documentación específica de tu software (como la Arquitectura).

## 🎯 Objetivo

Proveer los estándares comunes a todos los desarrollos:
1. **Gestión Automática de CHANGELOG**: Vía `release-please`.
2. **Documentación Obligatoria**: Requerimientos organizacionales.
3. **Flujo de Versionado**: SemVer y Conventional Commits.

> [!IMPORTANT]
> El uso de **Conventional Commits** es CRÍTICO. Sin él, el CHANGELOG no se generará automáticamente y se perderá la trazabilidad. Ver [Guía de Commits](docs/CONVENTIONAL_COMMITS.md).

## 📋 Requisitos de la Organización

👉 **[Leer Requerimientos Organizacionales (KPIs)](docs/ORGANIZATION_REQUIREMENTS.md)**

Resumen:
- **Licencia**: Apache 2.0.
- **Despliegue**: `Apolo_Dev` antes de producción.
- **Docs**: En inglés, con diagramas de arquitectura.

## 🛠️ Pasos para usar este template

1. **Copia la configuración de GitHub**:
   - `.github/workflows/release-please.yml`
   - `.github/release-please-config.json`
   - `.release-please-manifest.json`

2. **Crea tu documentación**:
   - Crea la carpeta `docs/`.
   - Crea `docs/ARCHITECTURE.md` siguiendo el [ejemplo incluido](docs/ARCHITECTURE.md).

3. **Desarrolla tu aplicación**:
   Crea tus fuentes y tests según el lenguaje elegido.

## 📄 Documentación Incluida

- [Requerimientos Organizacionales](docs/ORGANIZATION_REQUIREMENTS.md)
- [Arquitectura (Ejemplo)](docs/ARCHITECTURE.md)
- [Flujo de Release](docs/RELEASE_WORKFLOW.md)
- [Conventional Commits](docs/CONVENTIONAL_COMMITS.md)

## ⚖️ Licencia

Apache License 2.0 - Ver [LICENSE](LICENSE)
