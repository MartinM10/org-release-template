# Arquitectura del Proyecto

Todo proyecto debe tener un archivo `ARCHITECTURE.md` (o una carpeta `docs/architecture/`) que explique cómo funciona el sistema internamente.

## ¿Qué incluir?

Se recomienda encarecidamente el uso de diagramas **Mermaid** para ilustrar los conceptos.

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
# Arquitectura del Proyecto

## Visión General
Descripción de alto nivel...

## Diagrama de Componentes
(Insertar diagrama Mermaid aquí)

## Tecnologías
- Backend: ...
- Frontend: ...
- Base de Datos: ...

## Flujos de Datos Clave
Explicación de cómo viaja la información...

## Decisiones de Diseño (ADRs)
- Decisión 1: ...
- Decisión 2: ...
```
