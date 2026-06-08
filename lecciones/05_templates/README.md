# Lección 5: Plantillas en Django 📄

En esta lección, aprenderás sobre las plantillas en Django. Las plantillas definen cómo se muestra la información al usuario y te permiten crear interfaces dinámicas y reutilizables.

---

## 📌 ¿Qué son las plantillas?

En Django, una plantilla es un archivo de texto (generalmente HTML) que define la estructura y el diseño de una página web. Las plantillas pueden incluir etiquetas y filtros especiales que permiten insertar datos dinámicos y controlar el flujo de la página.

---

## 🛠️ Configuración de plantillas

### 1. Crear una carpeta de plantillas

Crea una carpeta llamada `templates` dentro de tu aplicación `mi_app`:

```bash
mkdir -p mi_app/templates/mi_app
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

## 📂 Estructura de una plantilla

### Ejemplo: Plantilla para listar libros

Crea un archivo llamado `lista_libros.html` dentro de `mi_app/templates/mi_app`:

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

### Explicación:

- **`{% for libro in libros %}`**: Etiqueta de plantilla para iterar sobre una lista de libros.
- **`{{ libro.titulo }}`**: Variable de plantilla para mostrar el título de un libro.

---

## 🔍 Etiquetas de plantilla

Las etiquetas de plantilla permiten controlar el flujo de la página y realizar operaciones lógicas.

### Ejemplo: Condicionales

```html
{% if libro.disponible %}
    <p>Disponible</p>
{% else %}
    <p>No disponible</p>
{% endif %}
```

### Ejemplo: Bucles

```html
<ul>
    {% for libro in libros %}
        <li>{{ libro.titulo }}</li>
    {% empty %}
        <li>No hay libros disponibles.</li>
    {% endfor %}
</ul>
```

---

## 📚 Filtros de plantilla

Los filtros de plantilla permiten modificar variables antes de mostrarlas.

### Ejemplo: Filtros comunes

```html
{{ libro.titulo|upper }}          <!-- Convierte a mayúsculas -->
{{ libro.fecha_publicacion|date:"Y-m-d" }}  <!-- Formatea la fecha -->
{{ libro.descripcion|truncatewords:10 }}  <!-- Trunca el texto a 10 palabras -->
```

---

## 🎯 Herencia de plantillas

La herencia de plantillas te permite crear una plantilla base y extenderla en otras plantillas. Esto es útil para evitar repetir código y mantener un diseño consistente.

### 1. Crear una plantilla base

Crea un archivo llamado `base.html` dentro de `mi_app/templates/mi_app`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Sitio Web{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Bienvenido a mi sitio web</h1>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        <p>© 2023 Mi Sitio Web</p>
    </footer>
</body>
</html>
```

### 2. Extender la plantilla base

Modifica `lista_libros.html` para extender la plantilla base:

```html
{% extends "mi_app/base.html" %}

{% block title %}Lista de Libros{% endblock %}

{% block content %}
    <h1>Lista de Libros</h1>
    <ul>
        {% for libro in libros %}
            <li>{{ libro.titulo }} - {{ libro.autor }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

---

## 📝 Inclusión de plantillas

La inclusión de plantillas te permite reutilizar partes de una plantilla en otras plantillas.

### 1. Crear una plantilla parcial

Crea un archivo llamado `navbar.html` dentro de `mi_app/templates/mi_app`:

```html
<nav>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/libros/">Libros</a></li>
        <li><a href="/contacto/">Contacto</a></li>
    </ul>
</nav>
```

### 2. Incluir la plantilla parcial

Modifica `base.html` para incluir la plantilla parcial:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Sitio Web{% endblock %}</title>
</head>
<body>
    {% include "mi_app/navbar.html" %}
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        <p>© 2023 Mi Sitio Web</p>
    </footer>
</body>
</html>
```

---

## 🎉 ¡Felicidades!

Has aprendido sobre las plantillas en Django y cómo crear interfaces dinámicas y reutilizables. En la próxima lección, aprenderás sobre las URLs y cómo configurar las rutas de tu aplicación.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊