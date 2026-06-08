# Lección 4: Vistas en Django 🌐

En esta lección, aprenderás sobre las vistas en Django. Las vistas son responsables de manejar la lógica de tu aplicación y devolver una respuesta al usuario.

---

## 📌 ¿Qué son las vistas?

En Django, una vista es una función o clase que recibe una solicitud HTTP y devuelve una respuesta HTTP. Las vistas pueden renderizar plantillas, redirigir a otras URLs, o devolver datos en formato JSON, entre otras cosas.

---

## 🛠️ Crear una vista

### Ejemplo: Vista para listar libros

Abre el archivo `mi_app/views.py` y define una vista llamada `lista_libros`:

```python
from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'mi_app/lista_libros.html', {'libros': libros})
```

### Explicación:

- **request**: El objeto de solicitud HTTP.
- **Libro.objects.all()**: Consulta todos los libros de la base de datos.
- **render**: Renderiza una plantilla y devuelve una respuesta HTTP.

---

## 📂 Plantillas

Las plantillas definen cómo se muestra la información al usuario. En Django, las plantillas suelen ser archivos HTML con etiquetas especiales que permiten insertar datos dinámicos.

### 1. Crear una plantilla

Crea una carpeta llamada `templates` dentro de tu aplicación `mi_app`:

```bash
mkdir -p mi_app/templates/mi_app
```

Dentro de esta carpeta, crea un archivo llamado `lista_libros.html`:

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

Abre `mi_proyecto/settings.py` y asegúrate de que la configuración de templates incluya la ruta a tu carpeta de templates:

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

## 🔍 Tipos de vistas

### Vistas basadas en funciones

Las vistas basadas en funciones son funciones de Python que reciben una solicitud y devuelven una respuesta:

```python
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Hola, mundo!")
```

### Vistas basadas en clases

Las vistas basadas en clases son clases de Python que heredan de `django.views.View` o alguna de sus subclases:

```python
from django.views import View
from django.http import HttpResponse

class HolaMundoView(View):
    def get(self, request):
        return HttpResponse("¡Hola, mundo!")
```

---

## 📚 Vistas genéricas

Django incluye vistas genéricas que puedes usar para realizar tareas comunes, como listar objetos, mostrar detalles de un objeto, crear, actualizar y eliminar objetos.

### Ejemplo: Vista genérica para listar libros

Abre `mi_app/views.py` y define una vista genérica:

```python
from django.views.generic import ListView
from .models import Libro

class ListaLibrosView(ListView):
    model = Libro
    template_name = 'mi_app/lista_libros.html'
    context_object_name = 'libros'
```

---

## 🎯 Manejo de formularios

### Crear un formulario

Crea un archivo llamado `forms.py` dentro de tu aplicación `mi_app`:

```python
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'disponible']
```

### Vista para crear un libro

Abre `mi_app/views.py` y define una vista para crear un libro:

```python
from django.shortcuts import render, redirect
from .forms import LibroForm

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'mi_app/crear_libro.html', {'form': form})
```

### Plantilla para crear un libro

Crea un archivo llamado `crear_libro.html` dentro de `mi_app/templates/mi_app`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Crear Libro</title>
</head>
<body>
    <h1>Crear Libro</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
```

---

## 🎉 ¡Felicidades!

Has aprendido sobre las vistas en Django y cómo manejar la lógica de tu aplicación. En la próxima lección, aprenderás sobre las URLs y cómo configurar las rutas de tu aplicación.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊