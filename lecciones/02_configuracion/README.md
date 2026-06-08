# Lección 2: Configuración Inicial 🛠️

En esta lección, aprenderás cómo configurar tu entorno de desarrollo y crear tu primer proyecto Django. ¡Vamos a poner las manos en el código! 💻

---

## 📌 Requisitos previos

Asegúrate de tener instalado Python en tu sistema. Puedes verificarlo ejecutando:

```bash
python --version
```

Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/).

---

## 🛠️ Instalación de Django

Instala Django usando pip, el gestor de paquetes de Python:

```bash
pip install django
```

Para verificar que Django se ha instalado correctamente, ejecuta:

```bash
python -m django --version
```

---

## 🚀 Crear un proyecto Django

Abre una terminal y ejecuta el siguiente comando para crear un nuevo proyecto Django:

```bash
django-admin startproject mi_proyecto
```

Esto creará una carpeta llamada `mi_proyecto` con la siguiente estructura:

```
mi_proyecto/
    manage.py          # Script para gestionar el proyecto
    mi_proyecto/
        __init__.py
        settings.py    # Configuración del proyecto
        urls.py        # Rutas principales
        asgi.py        # Configuración ASGI (para servidores asíncronos)
        wsgi.py        # Configuración WSGI (para servidores síncronos)
```

---

## 📂 Navegar al proyecto

Entra en la carpeta de tu proyecto:

```bash
cd mi_proyecto
```

---

## 🌐 Ejecutar el servidor de desarrollo

Django viene con un servidor de desarrollo integrado que puedes usar para probar tu aplicación localmente. Ejecuta el siguiente comando:

```bash
python manage.py runserver
```

Abre tu navegador y ve a [http://127.0.0.1:8000/](http://127.0.0.1:8000/). ¡Verás la página de bienvenida de Django!

---

## 📝 Configuración básica

### Archivo `settings.py`

El archivo `settings.py` contiene la configuración de tu proyecto. Aquí puedes configurar cosas como:

- **BASE_DIR**: La ruta base de tu proyecto.
- **SECRET_KEY**: Una clave secreta para la seguridad de tu proyecto.
- **DEBUG**: Modo de depuración (debe ser `True` en desarrollo y `False` en producción).
- **ALLOWED_HOSTS**: Lista de hosts permitidos para tu aplicación.
- **INSTALLED_APPS**: Lista de aplicaciones instaladas en tu proyecto.
- **DATABASES**: Configuración de la base de datos.

### Archivo `urls.py`

El archivo `urls.py` define las rutas de tu proyecto. Aquí puedes mapear URLs a vistas.

---

## 🎯 Crear una aplicación Django

En Django, un proyecto puede tener múltiples aplicaciones. Cada aplicación representa una funcionalidad específica (ej: blog, usuarios, tienda).

### 1. Crear una aplicación

Ejecuta el siguiente comando para crear una nueva aplicación:

```bash
python manage.py startapp mi_app
```

Esto creará una carpeta llamada `mi_app` con la siguiente estructura:

```
mi_app/
    __init__.py
    admin.py       # Configuración del panel de administración
    apps.py        # Configuración de la aplicación
    models.py      # Modelos de la base de datos
    tests.py       # Pruebas unitarias
    views.py       # Vistas de la aplicación
    migrations/   # Migraciones de la base de datos
```

### 2. Registrar la aplicación

Abre `mi_proyecto/settings.py` y agrega tu aplicación a `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'mi_app',
]
```

---

## 🎉 ¡Felicidades!

Has configurado tu entorno de desarrollo y creado tu primer proyecto Django. En la próxima lección, aprenderás sobre los modelos y cómo trabajar con bases de datos en Django.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊