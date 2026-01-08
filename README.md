# 📘 Guía de Referencia de Proyectos (Template)

Este repositorio sirve como **guía de referencia** estandarizada para proyectos de KHAOS / SEDIA.

## 📂 Estructura del Repositorio

Esta es la estructura base recomendada para todo proyecto:

```mermaid
graph TD
    Repo[Raíz del Proyecto] --> Docs[docs/]
    Repo --> Github[.github/]
    Repo --> Source[src/ o app/]
    Repo --> Tests[tests/]
    Repo --> Config files...
    
    Github --> Workflows[workflows/release-please.yml]
    Github --> Config[release-please-config.json]
    
    Docs --> Req[ORGANIZATION_REQUIREMENTS.md]
    Docs --> Arch[ARCHITECTURE.md]
    Docs --> Flow[RELEASE_WORKFLOW.md]
```

> **Nota**: Las carpetas `src/`, `tests/` o `app/` son placeholders. Debes crear la estructura que mejor se adapte a tu lenguaje (Python, Java, JS, etc.).

## 🎯 Objetivo

Proveer los estándares comunes a todos los desarrollos:
1. **Gestión Automática de CHANGELOG**: Vía `release-please`.
2. **Documentación Obligatoria**: Requerimientos organizacionales.
3. **Flujo de Versionado**: SemVer y Conventional Commits.

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

2. **Copia la documentación base**:
   - `CONTRIBUTING.md`
   - `docs/` (especialmente `ORGANIZATION_REQUIREMENTS.md`)

3. **Crea tu `ARCHITECTURE.md`**:
   Usa la [plantilla de arquitectura](docs/ARCHITECTURE_TEMPLATE.md) para documentar tu sistema con diagramas Mermaid.

4. **Desarrolla tu aplicación**:
   Crea tus fuentes y tests según el lenguaje elegido.

## 📄 Documentación Incluida

- [Requerimientos Organizacionales](docs/ORGANIZATION_REQUIREMENTS.md)
- [Plantilla de Arquitectura](docs/ARCHITECTURE_TEMPLATE.md)
- [Flujo de Release](docs/RELEASE_WORKFLOW.md)
- [Conventional Commits](docs/CONVENTIONAL_COMMITS.md)

## ⚖️ Licencia

Apache License 2.0 - Ver [LICENSE](LICENSE)
