# Lección 7: Panel de Administración de Django 🛠️

En esta lección, aprenderás sobre el panel de administración de Django. El panel de administración es una herramienta integrada que te permite gestionar los datos de tu aplicación de manera sencilla.

---

## 📌 ¿Qué es el panel de administración?

El panel de administración de Django es una interfaz web que te permite gestionar los datos de tu aplicación. Con él, puedes crear, leer, actualizar y eliminar registros de tus modelos sin tener que escribir código adicional.

---

## 🛠️ Configuración del panel de administración

### 1. Crear un superusuario

Para acceder al panel de administración, necesitas crear un superusuario. Ejecuta el siguiente comando:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un superusuario. Recuerda guardar tus credenciales en un lugar seguro.

### 2. Iniciar el servidor de desarrollo

Ejecuta el siguiente comando para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

### 3. Acceder al panel de administración

Abre tu navegador y ve a [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Inicia sesión con las credenciales del superusuario que creaste.

---

## 📂 Registrar modelos en el panel de administración

### 1. Registrar un modelo

Abre el archivo `mi_app/admin.py` y registra tu modelo:

```python
from django.contrib import admin
from .models import Libro

admin.site.register(Libro)
```

### 2. Personalizar el panel de administración

Puedes personalizar cómo se muestra tu modelo en el panel de administración creando una clase `ModelAdmin`:

```python
from django.contrib import admin
from .models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'disponible')
    list_filter = ('autor', 'disponible')
    search_fields = ('titulo', 'autor')
    date_hierarchy = 'fecha_publicacion'

admin.site.register(Libro, LibroAdmin)
```

### Explicación:

- **`list_display`**: Define los campos que se mostrarán en la lista de registros.
- **`list_filter`**: Define los campos por los que se puede filtrar la lista de registros.
- **`search_fields`**: Define los campos que se pueden buscar.
- **`date_hierarchy`**: Define un campo de fecha para navegar por jerarquía.

---

## 🔍 Personalización avanzada

### 1. Campos de solo lectura

Puedes definir campos de solo lectura en el panel de administración:

```python
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'disponible')
    readonly_fields = ('fecha_publicacion',)

admin.site.register(Libro, LibroAdmin)
```

### 2. Campos personalizados

Puedes definir métodos personalizados para mostrar información adicional en el panel de administración:

```python
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'disponible', 'dias_desde_publicacion')

    def dias_desde_publicacion(self, obj):
        return (timezone.now() - obj.fecha_publicacion).days

    dias_desde_publicacion.short_description = 'Días desde publicación'

admin.site.register(Libro, LibroAdmin)
```

---

## 📚 Relaciones en el panel de administración

### 1. Relación uno a muchos

Si tienes un modelo con una relación uno a muchos, puedes personalizar cómo se muestra en el panel de administración:

```python
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'disponible')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
```

### 2. Relación muchos a muchos

Si tienes un modelo con una relación muchos a muchos, puedes personalizar cómo se muestra en el panel de administración:

```python
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'disponible')
    filter_horizontal = ('autores',)

admin.site.register(Libro, LibroAdmin)
```

---

## 🎯 Personalizar el sitio de administración

### 1. Cambiar el título y encabezado

Puedes personalizar el título y el encabezado del panel de administración modificando el archivo `mi_proyecto/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Administración de Mi Proyecto"
admin.site.site_title = "Mi Proyecto Admin"
admin.site.index_title = "Bienvenido al panel de administración"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
]
```

### 2. Cambiar el estilo del panel de administración

Puedes personalizar el estilo del panel de administración creando un archivo CSS y cargándolo en tu proyecto. Para ello, sigue estos pasos:

1. Crea una carpeta llamada `static` dentro de tu aplicación `mi_app`:

```bash
mkdir -p mi_app/static/mi_app/css
```

2. Crea un archivo llamado `admin.css` dentro de `mi_app/static/mi_app/css`:

```css
/* Estilos personalizados para el panel de administración */
body {
    background-color: #f5f5f5;
}

#header {
    background-color: #333;
    color: #fff;
}
```

3. Crea un archivo llamado `admin.py` dentro de `mi_app` y define una clase para cargar el CSS:

```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

class AdminCSS:
    def __init__(self):
        self.css = {
            'all': ('mi_app/css/admin.css',)
        }

admin.site.index_template = 'admin/index.html'
admin.site.login_template = 'admin/login.html'
```

---

## 🎉 ¡Felicidades!

Has aprendido sobre el panel de administración de Django y cómo gestionar tus modelos. En la próxima lección, aprenderás sobre los formularios en Django y cómo manejar la entrada de datos de los usuarios.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊