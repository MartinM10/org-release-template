# Requerimientos Organizacionales (SEDIA / KHAOS)

Este documento detalla los criterios obligatorios que deben cumplir todos los repositorios de proyectos de la SEDIA y KHAOS.

## 📋 Criterios Generales

1. **Gestión en Git**: Todo código y documentación debe estar en un repositorio Git.
2. **Registro de Cambios**: Se debe mantener un historial detallado de versiones y cambios (CHANGELOG).
3. **Documentación Clara**:
   - Inglés técnico.
   - Especificaciones de desarrollo y despliegue.
   - Historial de cambios.
4. **Arquitectura**: Descripción detallada de arquitectura, tecnologías e interdependencias.
5. **Licencia**: Definida y documentada (Defecto: **Apache 2.0**).

## 📊 KPIs de Validación

Para validar el cumplimiento, se medirán los siguientes indicadores:

| KPI | Requisito Mínimo |
|-----|------------------|
| **Actividad** | Mínimo **100 commits** y **5 versiones etiquetadas**. |
| **Documentación** | Mínimo **1000 palabras** o 10 páginas (técnica + usuario + código). |
| **Actualización** | CHANGELOG actualizado al menos **cada 2 semanas** (en desarrollo activo). |
| **Despliegue** | 80% de implementaciones siguiendo estrategias documentadas. |

## 🚀 Estrategia de Despliegue y Pruebas

### Entorno de Desarrollo (Apolo_Dev)
- **IP**: `192.168.219.6`
- **Uso**: Pruebas de integración obligatorias antes de producción.
- **Requisito**: TODA implementación debe probarse aquí primero.
- **Red**: Las aplicaciones deben tener **IP privada**. No pueden apuntar a IPs públicas (ej: `150...`).

### Flujo de Aprobación
1. Desarrollo en rama local.
2. Despliegue/Pruebas en `Apolo_Dev`.
3. Verificación de funcionamiento e integración.
4. Despliegue a Producción (`Apolo`).

## 🛠️ Herramientas Estándar

- **Workflows**: GitHub Actions para despliegue, testing y changelog.
- **Changelog**: Usar `release-please` (ejemplo en este repo) o seguir modelo [KhaosResearch/EDAAnOWL](https://github.com/KhaosResearch/EDAAnOWL/blob/main/CHANGELOG.md).
- **Licencia**: Apache 2.0 por defecto (ver [LICENSE](../LICENSE)).

## 📄 Referencias

- Criterios de proyectos SEDIA.
- Directrices de arquitectura de KHAOS.
