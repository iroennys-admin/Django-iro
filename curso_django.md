# Curso Básico de Django por Iroennys Dev 🚀

¡Bienvenido a este curso de Django! Aquí aprenderás los conceptos básicos para crear aplicaciones web con Django, el framework más popular de Python. Este curso está diseñado para principiantes y está creado por **Iroennys Dev** con ejemplos prácticos y sencillos.

---

## 📌 Introducción a Django

Django es un framework de desarrollo web de alto nivel escrito en Python. Sigue el patrón **MTV** (Model-Template-View), que es una variante del clásico MVC (Model-View-Controller). Django te permite crear aplicaciones web rápidas, seguras y escalables con menos código.

### ¿Por qué Django?
- **Rápido desarrollo**: Django incluye muchas funcionalidades integradas (autenticación, administración, ORM, etc.).
- **Seguridad**: Protege contra vulnerabilidades comunes como SQL injection, CSRF, XSS, etc.
- **Escalable**: Usado por empresas como Instagram, Pinterest, Mozilla, entre otras.
- **Comunidad activa**: Gran cantidad de documentación, tutoriales y paquetes de terceros.

---

## 🛠️ Configuración Inicial

### 1. Instalar Python
Asegúrate de tener Python instalado (versión 3.6 o superior). Puedes verificarlo con:
```bash
python --version
```

### 2. Instalar Django
Instala Django usando pip:
```bash
pip install django
```

### 3. Crear un proyecto Django
Abre una terminal y ejecuta:
```bash
django-admin startproject mi_proyecto
cd mi_proyecto
```

### 4. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```
Abre tu navegador y ve a [http://127.0.0.1:8000/](http://127.0.0.1:8000/). ¡Verás la página de bienvenida de Django!

---

## 📂 Estructura del Proyecto

Un proyecto Django tiene la siguiente estructura básica:
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

## 🎨 Crear una Aplicación

En Django, un proyecto puede tener múltiples aplicaciones. Cada aplicación representa una funcionalidad específica (ej: blog, usuarios, tienda).

### 1. Crear una aplicación
```bash
python manage.py startapp mi_app
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

## 📝 Models (Modelos)

Los modelos definen la estructura de la base de datos. Cada modelo es una clase que hereda de `django.db.models.Model`.

### Ejemplo: Modelo `Libro`
En `mi_app/models.py`:
```python
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
```

### Crear y aplicar migraciones
1. Genera las migraciones:
   ```bash
   python manage.py makemigrations
   ```

2. Aplica las migraciones a la base de datos:
   ```bash
   python manage.py migrate
   ```

---

## 🌐 Views (Vistas)

Las vistas manejan la lógica de la aplicación y devuelven una respuesta al usuario.

### Ejemplo: Vista para listar libros
En `mi_app/views.py`:
```python
from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'mi_app/lista_libros.html', {'libros': libros})
```

---

## 📄 Templates (Plantillas)

Las plantillas definen cómo se muestra la información al usuario (HTML).

### 1. Crear un template
Crea una carpeta `templates/mi_app` dentro de tu aplicación y añade un archivo `lista_libros.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Libros</title>
</head>
<body>
    <h1>Lista de Libros</h1>
    <ul>
        {% for libro in libros %}
            <li>{{ libro.titulo }} - {{ libro.autor }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### 2. Configurar templates en `settings.py`
Asegúrate de que Django sepa dónde buscar los templates:
```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

---

## 🔗 URLs (Rutas)

Las URLs definen las rutas de tu aplicación y cómo se mapean a las vistas.

### 1. Configurar URLs de la aplicación
Crea un archivo `mi_app/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
]
```

### 2. Incluir URLs de la aplicación en el proyecto
En `mi_proyecto/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
]
```

---

## 📦 Admin de Django

Django incluye un panel de administración integrado para gestionar tus modelos.

### 1. Crear un superusuario
```bash
python manage.py createsuperuser
```

### 2. Registrar el modelo en el admin
En `mi_app/admin.py`:
```python
from django.contrib import admin
from .models import Libro

admin.site.register(Libro)
```

### 3. Acceder al admin
Ve a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) e inicia sesión con el superusuario.

---

## 🎉 ¡Felicidades!

Has completado los conceptos básicos de Django. Ahora puedes:
- Crear modelos y bases de datos.
- Definir vistas y templates.
- Configurar rutas.
- Usar el panel de administración.

### Próximos pasos
- Aprender sobre **formularios** en Django.
- Explorar **autenticación de usuarios**.
- Profundizar en **Django REST Framework** para APIs.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que este curso te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊