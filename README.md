# 📘 Guía de Referencia de Proyectos (Template)

Este repositorio sirve como **guía de referencia** para la creación y gestión de proyectos dentro de la organización (KHAOS / SEDIA).

> **Nota**: Este no es un template rígido para clonar tal cual, sino una demostración de la estructura y prácticas recomendadas. Debes adaptar estas recomendaciones a tu proyecto específico.

## 🎯 Objetivo

Proveer un ejemplo funcional de:
1. **Gestión automática de CHANGELOG** (vía `release-please`).
2. **Estructura de repositorio** estándar.
3. **Formato de commits** (Conventional Commits).
4. **Documentación de requisitos** organizacionales.

## 📋 Requisitos Obligatorios

Todos los proyectos deben cumplir con los criterios detallados en:
👉 [**Requerimientos Organizacionales**](docs/ORGANIZATION_REQUIREMENTS.md)

Resumen:
- **Licencia**: Apache 2.0.
- **Idioma**: Documentación en Inglés.
- **Despliegue**: Pruebas obligatorias en `Apolo_Dev` antes de producción.
- **KPIs**: Mínimo 100 commits, 5 tags, documentación extensa.

## 🛠️ Cómo Usar esta Guía

1. **Estructura tu Proyecto**:
   Inspírate en la organización de carpetas de este repo (`src`, `tests`, `docs`).

2. **Configura el Changelog Automático**:
   Copia `.github/workflows/release-please.yml` y `.github/release-please-config.json` a tu repositorio.
   Esto automatizará la creación del `CHANGELOG.md`.

3. **Adopta Conventional Commits**:
   Utiliza prefijos (`feat:`, `fix:`) en tus commits para que el changelog se genere correctamente.
   Ver [Guía de Commits](docs/CONVENTIONAL_COMMITS.md).

4. **Documenta tu Arquitectura**:
   Asegúrate de incluir documentación técnica detallada como se exige en los requisitos.

## 📄 Documentación Incluida

- [Requerimientos de la Organización](docs/ORGANIZATION_REQUIREMENTS.md)
- [Guía de Conventional Commits](docs/CONVENTIONAL_COMMITS.md)
- [Flujo de Release (release-please)](docs/RELEASE_WORKFLOW.md)
- [Protección de Ramas](docs/BRANCH_PROTECTION.md)

## ⚖️ Licencia

Apache License 2.0 - Ver [LICENSE](LICENSE)
