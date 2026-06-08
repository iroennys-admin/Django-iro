# Lección 3: Modelos en Django 📝

En esta lección, aprenderás sobre los modelos en Django. Los modelos definen la estructura de tu base de datos y te permiten interactuar con ella de manera sencilla.

---

## 📌 ¿Qué son los modelos?

En Django, un modelo es una clase que hereda de `django.db.models.Model`. Cada modelo representa una tabla en la base de datos, y cada atributo de la clase representa un campo en esa tabla.

---

## 🛠️ Crear un modelo

### Ejemplo: Modelo `Libro`

Abre el archivo `mi_app/models.py` y define un modelo llamado `Libro`:

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

### Explicación de los campos:

- **CharField**: Campo de texto con una longitud máxima.
- **DateField**: Campo de fecha.
- **BooleanField**: Campo booleano (True/False).

---

## 📂 Migraciones

Las migraciones son la manera en que Django propaga los cambios que haces en tus modelos (agregar un campo, eliminar un modelo, etc.) a tu esquema de base de datos.

### 1. Crear una migración

Ejecuta el siguiente comando para crear una migración basada en los cambios en tus modelos:

```bash
python manage.py makemigrations
```

### 2. Aplicar la migración

Ejecuta el siguiente comando para aplicar la migración a tu base de datos:

```bash
python manage.py migrate
```

---

## 🔍 Operaciones con modelos

### Crear un registro

Puedes crear un nuevo registro en la base de datos de la siguiente manera:

```python
from mi_app.models import Libro

libro = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", fecha_publicacion="1967-05-30")
libro.save()
```

### Consultar registros

Puedes consultar registros de la base de datos usando el administrador de objetos del modelo:

```python
# Obtener todos los libros
libros = Libro.objects.all()

# Obtener un libro por su título
libro = Libro.objects.get(titulo="Cien años de soledad")

# Filtrar libros por autor
libros = Libro.objects.filter(autor="Gabriel García Márquez")
```

### Actualizar un registro

Puedes actualizar un registro de la siguiente manera:

```python
libro = Libro.objects.get(titulo="Cien años de soledad")
libro.disponible = False
libro.save()
```

### Eliminar un registro

Puedes eliminar un registro de la siguiente manera:

```python
libro = Libro.objects.get(titulo="Cien años de soledad")
libro.delete()
```

---

## 📚 Tipos de campos comunes

Aquí tienes algunos tipos de campos comunes que puedes usar en tus modelos:

- **CharField**: Campo de texto con una longitud máxima.
- **TextField**: Campo de texto largo.
- **IntegerField**: Campo numérico entero.
- **FloatField**: Campo numérico de punto flotante.
- **DateField**: Campo de fecha.
- **DateTimeField**: Campo de fecha y hora.
- **BooleanField**: Campo booleano (True/False).
- **EmailField**: Campo de correo electrónico.
- **URLField**: Campo de URL.
- **ForeignKey**: Campo de clave foránea para relaciones entre modelos.

---

## 🎯 Relaciones entre modelos

### Relación uno a muchos

Puedes definir una relación uno a muchos usando `ForeignKey`:

```python
class Autor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
```

### Relación muchos a muchos

Puedes definir una relación muchos a muchos usando `ManyToManyField`:

```python
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
```

---

## 🎉 ¡Felicidades!

Has aprendido sobre los modelos en Django y cómo interactuar con la base de datos. En la próxima lección, aprenderás sobre las vistas y cómo manejar la lógica de tu aplicación.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊