# Lección 8: Formularios en Django 📝

En esta lección, aprenderás sobre los formularios en Django. Los formularios te permiten manejar la entrada de datos de los usuarios y validarlos antes de procesarlos.

---

## 📌 ¿Qué son los formularios?

En Django, un formulario es una clase que hereda de `django.forms.Form` o `django.forms.ModelForm`. Los formularios te permiten definir campos, validar datos y renderizar formularios HTML.

---

## 🛠️ Crear un formulario

### 1. Formulario básico

Crea un archivo llamado `forms.py` dentro de tu aplicación `mi_app`:

```python
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
```

### Explicación:

- **`CharField`**: Campo de texto con una longitud máxima.
- **`EmailField`**: Campo de correo electrónico.
- **`widget=forms.Textarea`**: Define el widget para renderizar el campo como un área de texto.

---

## 📂 Renderizar un formulario

### 1. Crear una vista para el formulario

Abre `mi_app/views.py` y define una vista para manejar el formulario:

```python
from django.shortcuts import render
from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            # Aquí puedes guardar los datos en la base de datos o enviar un correo electrónico
            return render(request, 'mi_app/gracias.html', {'nombre': nombre})
    else:
        form = ContactoForm()
    return render(request, 'mi_app/contacto.html', {'form': form})
```

### 2. Crear una plantilla para el formulario

Crea un archivo llamado `contacto.html` dentro de `mi_app/templates/mi_app`:

```html
{% extends "mi_app/base.html" %}

{% block title %}Contacto{% endblock %}

{% block content %}
    <h1>Contacto</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Enviar</button>
    </form>
{% endblock %}
```

### 3. Crear una plantilla de agradecimiento

Crea un archivo llamado `gracias.html` dentro de `mi_app/templates/mi_app`:

```html
{% extends "mi_app/base.html" %}

{% block title %}Gracias{% endblock %}

{% block content %}
    <h1>Gracias, {{ nombre }}!</h1>
    <p>Tu mensaje ha sido enviado correctamente.</p>
{% endblock %}
```

---

## 🔍 Validación de formularios

### 1. Validación básica

Django realiza validación básica automáticamente según el tipo de campo. Por ejemplo, `EmailField` valida que el correo electrónico tenga un formato válido.

### 2. Validación personalizada

Puedes agregar validación personalizada a tus formularios definiendo un método `clean_<nombre_del_campo>`:

```python
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre
```

---

## 📚 Formularios basados en modelos

### 1. Crear un formulario basado en un modelo

Puedes crear un formulario basado en un modelo para simplificar la creación de formularios que guardan datos en la base de datos:

```python
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'disponible']
```

### 2. Crear una vista para el formulario basado en modelo

Abre `mi_app/views.py` y define una vista para manejar el formulario:

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

### 3. Crear una plantilla para el formulario basado en modelo

Crea un archivo llamado `crear_libro.html` dentro de `mi_app/templates/mi_app`:

```html
{% extends "mi_app/base.html" %}

{% block title %}Crear Libro{% endblock %}

{% block content %}
    <h1>Crear Libro</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
{% endblock %}
```

---

## 🎯 Personalización de formularios

### 1. Personalizar widgets

Puedes personalizar los widgets de tus formularios para cambiar cómo se renderizan los campos:

```python
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'disponible']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
        }
```

### 2. Personalizar etiquetas y ayuda

Puedes personalizar las etiquetas y la ayuda de tus formularios:

```python
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'disponible']
        labels = {
            'titulo': 'Título del libro',
            'autor': 'Autor del libro',
        }
        help_texts = {
            'fecha_publicacion': 'Formato: YYYY-MM-DD',
        }
```

---

## 🎉 ¡Felicidades!

Has aprendido sobre los formularios en Django y cómo manejar la entrada de datos de los usuarios. En la próxima lección, aprenderás sobre el despliegue de aplicaciones Django y cómo llevar tu proyecto a producción.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊