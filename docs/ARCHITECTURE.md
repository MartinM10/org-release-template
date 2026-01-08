# Arquitectura del Proyecto

Todo proyecto debe tener un archivo `ARCHITECTURE.md` que podría estar en la raíz del proyecto o en una carpeta `docs/architecture/` que explique cómo funciona el sistema internamente, qué componentes tiene, y cómo se comunican entre ellos.

## ¿Qué incluir?

`Se recomienda` el uso de diagramas, ya sean ficheros .png o .svg, o diagramas **Mermaid** para ilustrar los conceptos y que sean fáciles de entender.
> [!NOTE]
> A continuación se muestran algunos ejemplos de diagramas mermaid que puedes usar:

### 1. Diagrama de Contexto (C4 Nivel 1)
Muestra cómo el sistema interactúa con usuarios y otros sistemas externos.

```mermaid
C4Context
    title Diagrama de Contexto del Sistema
    
    Person(user, "Usuario", "Usa el aplicativo web")
    System(sistema, "Nuestro Sistema", "Provee servicios de XYZ")
    System_Ext(auth, "Auth Provider", "Gestión de identidades")
    
    Rel(user, sistema, "Usa", "HTTPS")
    Rel(sistema, auth, "Valida token", "OIDC")
```

### 2. Diagrama de Contenedores (C4 Nivel 2)
Muestra las aplicaciones, servicios de datos y microservicios.

```mermaid
C4Container
    title Diagrama de Contenedores
    
    Container(spa, "SPA", "React", "Interfaz de usuario")
    Container(api, "API Layer", "Python/FastAPI", "Lógica de negocio")
    ContainerDb(db, "Database", "PostgreSQL", "Almacenamiento")
    
    Rel(spa, api, "Llamadas API", "JSON/HTTPS")
    Rel(api, db, "Lee/Escribe", "SQL/TCP")
```

### 3. Diagrama de Secuencia
Para explicar flujos complejos específicos.

```mermaid
sequenceDiagram
    participant U as Usuario
    participant A as API
    participant D as DB
    
    U->>A: Solicita datos
    A->>D: Query
    D-->>A: Resultados
    A-->>U: JSON Response
```

## Plantilla Sugerida

Puedes copiar el siguiente contenido a tu `ARCHITECTURE.md`:

```markdown
# Project Architecture

## Overview
Descripción de alto nivel...

Podrías explicar el propósito del proyecto, las principales funcionalidades y cómo se relacionan entre sí.

## Components Diagram
(Insertar diagrama Mermaid aquí)

Podrías explicar los componentes principales del sistema y cómo se relacionan entre sí.

## Technologies
Podrías listar las tecnologías principales que se usan en el proyecto.

- Backend: ...
- Frontend: ...
- Base de Datos: ...

## Design Decisions
Podrías explicar las decisiones de diseño que se tomaron para el proyecto.

- Decision 1: ...
- Decision 2: ...
```
