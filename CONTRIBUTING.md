# Guía de Contribución

¡Gracias por tu interés en contribuir! 🎉

## 📋 Antes de Empezar

1. Lee la documentación en [/docs](docs/)
2. Familiarízate con [Conventional Commits](docs/CONVENTIONAL_COMMITS.md)
3. Asegúrate de tener Node.js 20+ instalado

## 🔧 Setup del Entorno

```bash
# Clonar el repositorio
git clone https://github.com/org/repo.git
cd repo

# Instalar dependencias
npm install

# Verificar que todo funciona
npm run lint
npm test
```

## 🌿 Flujo de Trabajo (Git Flow)

### 1. Crear Branch

```bash
# Actualizar main
git checkout main
git pull origin main

# Crear nueva branch
git checkout -b tipo/descripcion
```

**Nombres de branch recomendados:**
- `feature/add-login`
- `fix/resolve-timeout`
- `docs/update-readme`

### 2. Hacer Cambios

Escribe código limpio siguiendo las guías de estilo del proyecto.

### 3. Commits

**Formato obligatorio: [Conventional Commits](docs/CONVENTIONAL_COMMITS.md)**

```bash
# Estructura
<tipo>[ámbito opcional]: <descripción>

# Ejemplos
git commit -m "feat: add user authentication"
git commit -m "fix(api): resolve timeout in login endpoint"
git commit -m "docs: update installation guide"
```

**Tipos válidos:**
| Tipo | Uso |
|------|-----|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de bug |
| `docs` | Documentación |
| `style` | Formato (sin cambio lógico) |
| `refactor` | Reestructurar código |
| `perf` | Mejora de rendimiento |
| `test` | Tests |
| `build` | Build/dependencias |
| `ci` | CI/CD |
| `chore` | Mantenimiento |

### 4. Crear Pull Request

1. Push tu branch: `git push origin tu-branch`
2. Ve a GitHub y crea un PR hacia `main`
3. **El título del PR DEBE seguir Conventional Commits**
4. Completa la plantilla del PR
5. Espera la revisión

### 5. Code Review

- Responde a los comentarios
- Haz los cambios solicitados
- Mantén tu branch actualizada con main:
  ```bash
  git fetch origin main
  git rebase origin/main
  ```

### 6. Merge

Una vez aprobado y con CI verde, tu PR será mergeado.

## ✅ Checklist del PR

Antes de solicitar revisión:

- [ ] Mi código sigue las guías de estilo
- [ ] He añadido tests (si aplica)
- [ ] Los tests pasan localmente (`npm test`)
- [ ] El lint pasa (`npm run lint`)
- [ ] He actualizado la documentación (si aplica)
- [ ] El título del PR sigue Conventional Commits

## 🚫 Lo que NO debes hacer

- ❌ Hacer push directo a `main`
- ❌ Force push a branches compartidas
- ❌ Commits con mensajes como "fix" o "update"
- ❌ PRs muy grandes (divide en PRs pequeños)
- ❌ Ignorar comentarios de revisión

## 🆘 ¿Necesitas Ayuda?

- Revisa la [documentación](docs/)
- Pregunta en el canal de Slack del equipo
- Menciona a un maintainer en tu PR

## 📜 Código de Conducta

- Sé respetuoso y profesional
- Acepta feedback constructivo
- Ayuda a otros cuando puedas
