# Lección 6: URLs en Django 🔗

En esta lección, aprenderás sobre las URLs en Django. Las URLs definen las rutas de tu aplicación y cómo se mapean a las vistas.

---

## 📌 ¿Qué son las URLs?

En Django, las URLs son patrones que definen cómo se mapean las solicitudes HTTP a las vistas. Cada URL puede estar asociada a una vista específica, que se encarga de manejar la lógica de la solicitud y devolver una respuesta.

---

## 🛠️ Configuración de URLs

### 1. Archivo `urls.py` del proyecto

El archivo `urls.py` en la carpeta de tu proyecto (`mi_proyecto/urls.py`) define las rutas principales de tu aplicación. Aquí puedes incluir las URLs de tus aplicaciones.

### Ejemplo: Incluir URLs de una aplicación

Abre `mi_proyecto/urls.py` y modifícalo para incluir las URLs de tu aplicación:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
]
```

---

## 📂 Archivo `urls.py` de la aplicación

### 1. Crear un archivo `urls.py` para tu aplicación

Crea un archivo llamado `urls.py` dentro de tu aplicación `mi_app`:

```bash
touch mi_app/urls.py
```

### 2. Definir las URLs de la aplicación

Abre `mi_app/urls.py` y define las URLs de tu aplicación:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
]
```

### Explicación:

- **`path('libros/', views.lista_libros, name='lista_libros')`**: Define una ruta para la vista `lista_libros`.
- **`name='lista_libros'`**: Asigna un nombre a la URL para referenciarla fácilmente en tus plantillas y vistas.

---

## 🔍 Parámetros en URLs

Puedes definir parámetros en tus URLs para capturar valores dinámicos.

### Ejemplo: URL con parámetro

```python
from django.urls import path
from . import views

urlpatterns = [
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
]
```

### Vista para manejar el parámetro

Abre `mi_app/views.py` y define una vista para manejar el parámetro:

```python
from django.shortcuts import render, get_object_or_404
from .models import Libro

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'mi_app/detalle_libro.html', {'libro': libro})
```

### Plantilla para mostrar el detalle del libro

Crea un archivo llamado `detalle_libro.html` dentro de `mi_app/templates/mi_app`:

```html
{% extends "mi_app/base.html" %}

{% block title %}Detalle del Libro{% endblock %}

{% block content %}
    <h1>{{ libro.titulo }}</h1>
    <p>Autor: {{ libro.autor }}</p>
    <p>Fecha de publicación: {{ libro.fecha_publicacion }}</p>
    <p>Disponible: {% if libro.disponible %}Sí{% else %}No{% endif %}</p>
{% endblock %}
```

---

## 📚 Nombres de URLs

Los nombres de URLs te permiten referenciar URLs en tus plantillas y vistas sin tener que escribir la URL completa. Esto es útil para evitar errores y hacer tu código más mantenible.

### Ejemplo: Usar nombres de URLs en plantillas

```html
<a href="{% url 'lista_libros' %}">Ver lista de libros</a>
<a href="{% url 'detalle_libro' libro.id %}">Ver detalle</a>
```

### Ejemplo: Usar nombres de URLs en vistas

```python
from django.shortcuts import redirect
from django.urls import reverse

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_libros'))
    else:
        form = LibroForm()
    return render(request, 'mi_app/crear_libro.html', {'form': form})
```

---

## 🎯 Espacios de nombres de URLs

Los espacios de nombres de URLs te permiten organizar tus URLs y evitar conflictos de nombres. Esto es especialmente útil en proyectos grandes con múltiples aplicaciones.

### Ejemplo: Definir un espacio de nombres

Abre `mi_app/urls.py` y define un espacio de nombres:

```python
from django.urls import path
from . import views

app_name = 'mi_app'

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
]
```

### Ejemplo: Usar espacios de nombres en plantillas

```html
<a href="{% url 'mi_app:lista_libros' %}">Ver lista de libros</a>
<a href="{% url 'mi_app:detalle_libro' libro.id %}">Ver detalle</a>
```

---

## 🎉 ¡Felicidades!

Has aprendido sobre las URLs en Django y cómo configurar las rutas de tu aplicación. En la próxima lección, aprenderás sobre el panel de administración de Django y cómo gestionar tus modelos.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊