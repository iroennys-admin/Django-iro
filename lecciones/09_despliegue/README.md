# Lección 9: Despliegue de Aplicaciones Django 🚀

En esta lección, aprenderás sobre el despliegue de aplicaciones Django. El despliegue es el proceso de llevar tu aplicación desde el entorno de desarrollo a un entorno de producción, donde los usuarios finales pueden acceder a ella.

---

## 📌 ¿Qué es el despliegue?

El despliegue es el proceso de instalar, configurar y ejecutar tu aplicación en un servidor para que esté disponible para los usuarios finales. Esto implica configurar un servidor web, una base de datos, y otros servicios necesarios para que tu aplicación funcione correctamente.

---

## 🛠️ Preparación para el despliegue

### 1. Configuración de `settings.py`

Antes de desplegar tu aplicación, debes asegurarte de que la configuración de tu proyecto sea adecuada para un entorno de producción. Abre `mi_proyecto/settings.py` y realiza los siguientes cambios:

```python
# Desactivar el modo de depuración
DEBUG = False

# Configurar hosts permitidos
ALLOWED_HOSTS = ['tu-dominio.com', 'tu-ip-del-servidor']

# Configurar la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_la_base_de_datos',
        'USER': 'nombre_de_usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configurar archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Configurar archivos de medios
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

---

## 📂 Despliegue en un servidor

### 1. Elección del servidor

Puedes desplegar tu aplicación en varios tipos de servidores, como:

- **Servidores VPS**: DigitalOcean, Linode, Vultr, etc.
- **Servidores en la nube**: AWS, Google Cloud, Azure, etc.
- **Plataformas de hosting**: PythonAnywhere, Heroku, etc.

### 2. Configuración del servidor

#### Instalar dependencias

Conéctate a tu servidor mediante SSH y ejecuta los siguientes comandos para instalar las dependencias necesarias:

```bash
# Actualizar paquetes
sudo apt update
sudo apt upgrade

# Instalar Python y pip
sudo apt install python3 python3-pip python3-venv

# Instalar un servidor web (Nginx)
sudo apt install nginx

# Instalar una base de datos (PostgreSQL)
sudo apt install postgresql postgresql-contrib

# Instalar Git
sudo apt install git
```

#### Configurar la base de datos

1. Conéctate a PostgreSQL:

```bash
sudo -u postgres psql
```

2. Crea una base de datos y un usuario:

```sql
CREATE DATABASE nombre_de_la_base_de_datos;
CREATE USER nombre_de_usuario WITH PASSWORD 'contraseña';
GRANT ALL PRIVILEGES ON DATABASE nombre_de_la_base_de_datos TO nombre_de_usuario;
ALTER ROLE nombre_de_usuario SET client_encoding TO 'utf8';
ALTER ROLE nombre_de_usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE nombre_de_usuario SET timezone TO 'UTC';
```

3. Sal de PostgreSQL:

```sql\q
```

---

## 🔍 Despliegue con Gunicorn

Gunicorn es un servidor WSGI para Python que puedes usar para ejecutar tu aplicación Django en producción.

### 1. Instalar Gunicorn

Ejecuta el siguiente comando para instalar Gunicorn:

```bash
pip install gunicorn
```

### 2. Configurar Gunicorn

Crea un archivo llamado `gunicorn.conf.py` en la raíz de tu proyecto:

```python
bind = "0.0.0.0:8000"
workers = 3
timeout = 120
```

### 3. Ejecutar Gunicorn

Ejecuta el siguiente comando para iniciar Gunicorn:

```bash
gunicorn mi_proyecto.wsgi:application --config gunicorn.conf.py
```

---

## 📚 Despliegue con Nginx

Nginx es un servidor web que puedes usar como proxy inverso para tu aplicación Django.

### 1. Configurar Nginx

Crea un archivo de configuración para Nginx en `/etc/nginx/sites-available/mi_proyecto`:

```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /ruta/a/tu/proyecto;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/ruta/a/tu/proyecto/mi_proyecto.sock;
    }
}
```

### 2. Habilitar el sitio

Ejecuta los siguientes comandos para habilitar el sitio:

```bash
sudo ln -s /etc/nginx/sites-available/mi_proyecto /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🎯 Despliegue en Heroku

Heroku es una plataforma de hosting que te permite desplegar aplicaciones Django de manera sencilla.

### 1. Instalar el CLI de Heroku

Descarga e instala el CLI de Heroku desde [heroku.com](https://devcenter.heroku.com/articles/heroku-cli).

### 2. Crear un archivo `Procfile`

Crea un archivo llamado `Procfile` en la raíz de tu proyecto:

```
web: gunicorn mi_proyecto.wsgi --log-file -
```

### 3. Crear un archivo `requirements.txt`

Ejecuta el siguiente comando para generar un archivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

### 4. Crear un archivo `runtime.txt`

Crea un archivo llamado `runtime.txt` en la raíz de tu proyecto:

```
python-3.8.10
```

### 5. Desplegar en Heroku

Ejecuta los siguientes comandos para desplegar tu aplicación en Heroku:

```bash
heroku login
heroku create
git push heroku master
heroku run python manage.py migrate
heroku open
```

---

## 🎉 ¡Felicidades!

Has aprendido sobre el despliegue de aplicaciones Django y cómo llevar tu proyecto a producción. Ahora puedes compartir tu aplicación con el mundo y permitir que los usuarios finales la utilicen.

---

**Creador:** Iroennys Dev 💻
**GitHub:** [iroennys-admin](https://github.com/iroennys-admin)

¡Espero que esta lección te haya sido útil! Si tienes dudas, no dudes en contactarme. 😊