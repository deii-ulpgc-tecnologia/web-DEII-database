# Guía de Flujo de Trabajo en Git

Para mantener un historial de cambios limpio, organizado y fácil de leer, seguimos una serie de convenciones tanto para la creación de ramas como para la estructura de los commits.

---

## 📋 Índice

- [Nomenclatura de Ramas](#nomenclatura-de-ramas)
  - [Estructura de Nombre de Rama](#estructura-de-nombre-de-rama)
  - [Cómo crear una rama en el IDE (PyCharm)](#cómo-crear-una-rama-en-el-ide-pycharm)
- [Nomenclatura para Commits](#nomenclatura-para-commits)
  - [Estructura de un Commit](#estructura-de-un-commit)
  - [Tipos de Commits](#tipos-de-commits)
  - [Ejemplos de Comparación](#ejemplos-de-comparación)
- [Flujo de Integración (Pull Requests)](#flujo-de-integración-pull-requests)

---

## Nomenclatura de Ramas

Cuando se va a trabajar en una nueva funcionalidad, corrección de errores o tarea, se debe crear una rama independiente a partir de la rama de desarrollo activa (normalmente `unstable`).

### Estructura de Nombre de Rama

El nombre de la rama debe estar asociado a una **Historia de Usuario (User Story)** o **Ticket**, utilizando la siguiente convención:


![alt text](assets/create_branch.png)





### Cómo crear una rama en el IDE (PyCharm)

1. En el menú superior o en la barra de estado de Git del IDE, abre el selector de ramas y selecciona **New Branch...**:
   
   ![Abrir menú de nueva rama](assets/new_branch.png)

2. Introduce el nombre de la rama siguiendo el formato acordado y haz clic en **Create**:
   
   ![Crear nueva rama](assets/new_branch_name.png)

---

## Nomenclatura para Commits

Para los commits del proyecto, utilizamos una convención simplificada basada en *Conventional Commits*.

### Estructura de un Commit

El formato básico debe ser el siguiente:

```text
<tipo> (<ámbito>): <descripción breve>
```

- **tipo**: La categoría del cambio que estás realizando (ver abajo).
- **ámbito** *(opcional)*: La sección del proyecto o módulo afectado (ej. `files`, `database`, `api`, `news`).
- **descripción**: Un resumen corto del cambio. Preferiblemente en minúsculas, usando verbos en imperativo/infinitivo (ej. "create", "add", "fix") y sin punto al final.

---

### Tipos de Commits

Estos son los prefijos que debes utilizar según el cambio realizado:

- **`feat`** (Feature): Añade una nueva funcionalidad o característica al proyecto.
  - *Ejemplo:* `feat (users): create a account`
  - *Ejemplo:* `feat (news): add image upload for articles`

- **`fix`** (Bug Fix): Soluciona un error o un bug en el código.
  - *Ejemplo:* `fix (auth): resolve login error with empty passwords`

- **`docs`** (Documentation): Cambios que solo afectan a la documentación (archivos README, guías de configuración, etc.).
  - *Ejemplo:* `docs (setup): update project installation guide`

- **`style`** (Style): Cambios visuales o de formato en el código que no afectan su funcionamiento (espacios, indentación, comillas).
  - *Ejemplo:* `style (models): format python classes with black`

- **`refactor`** (Refactor): Cambios en el código que no añaden funcionalidades ni corrigen errores, pero mejoran la estructura o limpieza (ej. renombrar variables, simplificar funciones).
  - *Ejemplo:* `refactor (database): optimize user search query`

- **`test`** (Test): Añadir pruebas nuevas o corregir pruebas existentes.
  - *Ejemplo:* `test (users): add unit test for account creation`

- **`chore`** (Chore): Tareas de mantenimiento, actualización de dependencias (paquetes), configuración del entorno o herramientas.
  - *Ejemplo:* `chore (deps): update django version in requirements.txt`

---

### Ejemplos de Comparación

✅ **Correctos:**
- `feat (subjects): add new endpoint to list subjects`
- `fix (database): correct foreign key in comments model`
- `chore: clean up unused assets` *(el ámbito es opcional)*

❌ **Incorrectos:**
- `Update users` *(No especifica el tipo)*
- `feat: CREATED LOGIN PAGE.` *(Uso de mayúsculas, verbo en pasado y punto final)*
- `fixed a bug in subjects view` *(No usa el formato correcto, debería ser `fix (subjects): ...`)*


## Flujo de Integración (Pull Requests)

Una vez que se termine de programar la funcionalidad o corrección en su rama, se debe realizar un Pull Request para fusionarla con la rama de desarrollo activa (normalmente `unstable`).

> [!IMPORTANT]
> **Antes de realizar un Pull Request:**
> 1. **Pruebas Locales:** Asegúrate de ejecutar y superar todas las pruebas (tests) necesarias localmente.
> 2. **Eliminación de Ramas:** Una vez que el Pull Request sea aprobado y fusionado, la rama correspondiente debe eliminarse del repositorio remoto para mantener el historial limpio y ordenado.

![Abrir Pull Request](assets/open_pull_request.png)