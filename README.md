# 🏛️ web-DEII-database

Backend de la base de datos y API para la página web de la **Delegación de Estudiantes de la Escuela de Ingeniería Informática (DEII)** de la ULPGC. 

Este proyecto está construido con **Django 6.0** y **Django REST Framework (DRF)**, exponiendo servicios REST autenticados mediante **JWT (JSON Web Tokens)** para gestionar contenidos de la delegación como asignaturas, noticias, archivos y control de usuarios.

---

## 📋 Índice

- [📂 Estructura del Proyecto](#-estructura-del-proyecto)
- [🛠️ Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [🚀 Instalación y Configuración Rápida](#-instalación-y-configuración-rápida)
- [🔄 Flujo de Trabajo en Git](#-flujo-de-trabajo-en-git)

---

## 📂 Estructura del Proyecto

El proyecto está organizado en diferentes aplicaciones de Django para mantener una arquitectura modular y escalable:

```text
web-DEII-database/
├── docs/                     # Documentación general del proyecto
│   ├── git-workflow/         # Guía de estilo de Git (ramas y commits)
│   └── setup/                # Guía de preparación del entorno de desarrollo
├── web_deii_project/         # Configuración global del proyecto Django (settings, urls, wsgi)
│   └── settings/             # Ajustes divididos por entornos (base, dev, prod, test)
├── web_deii_app/             # Aplicación principal (Usuarios, Autenticación, FAQs)
├── files_app/                # Gestión de subida, aprobación y etiquetado de archivos
├── subjects_app/             # Gestión de asignaturas académicas, cursos y semestres
├── news_app/                 # Gestión de noticias, anuncios y posts informativos
├── manage.py                 # Script de administración de Django
├── pyproject.toml / uv.lock  # Configuración y bloqueo de dependencias (para gestor 'uv')
└── requirements.txt          # Dependencias del proyecto para 'pip'
```

### Detalle de las Aplicaciones

*   **`web_deii_project`**: Contiene la configuración base del proyecto. Las configuraciones están modularizadas en `settings/base.py` (común), `settings/dev.py` (desarrollo), `settings/prod.py` (producción) y `settings/test.py` (pruebas).
*   **`web_deii_app`**: Gestiona los usuarios personalizados (`User`) con roles como `is_comunicacion` e `is_estudios`. También administra el sistema de autenticación basado en JWT y las preguntas frecuentes (`Faq`). Expone las rutas base de la API bajo el prefijo `/api/`.
*   **`files_app`**: Se encarga del flujo de subida de archivos (apuntes, exámenes, etc.). Incluye control de estados (pendiente, aprobado, rechazado), aprobaciones por parte de moderadores y etiquetado (`File` y `Tag`). Expone sus rutas bajo `/files/`.
*   **`subjects_app`**: Almacena las asignaturas asociadas a las diferentes titulaciones, años académicos y semestres (`Subject`). Expone sus rutas bajo `/subjects/`.
*   **`news_app`**: Permite la publicación de noticias en la web, con soporte para fijar artículos (`pinned`) y control de estado de publicación (`is_active`). Expone sus rutas bajo `/news/`.

---

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.12.x
*   **Framework Web:** [Django 6.0.3](https://docs.djangoproject.com/en/6.0/)
*   **API REST:** [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
*   **Autenticación:** JWT con [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)
*   **Base de Datos:** PostgreSQL
*   **Gestor de Paquetes:** `uv` / `pip`

---

## 🚀 Instalación y Configuración Rápida

Para poner en marcha el proyecto localmente, sigue estos pasos básicos (para una guía más detallada paso a paso e integración con el IDE, consulta la **[Guía de Preparación del Entorno](docs/setup/setup.md)**):


## 🔄 Flujo de Trabajo en Git

Para contribuir al desarrollo del proyecto de forma ordenada, es obligatorio cumplir las siguientes normas:

*   **Creación de Ramas**: Cada funcionalidad o corrección debe desarrollarse en su propia rama con el prefijo del ticket/historia asociado (ej. `(ejemplos)`).
*   **Mensajes de Commit**: Deben seguir la especificación simplificada de *Conventional Commits* (ej. `feat (users): add login view`).

👉 Consulta todos los detalles y ejemplos en la **[Guía de Flujo de Trabajo en Git](docs/git-workflow/git-workflow.md)**.



