#!/usr/bin/env python3

import os
import markdown

# Directorio de lecciones
LESSONS_DIR = "lecciones"
DOCS_DIR = "docs"

# Crear directorio para lecciones en docs
LESSONS_DOCS_DIR = os.path.join(DOCS_DIR, "lecciones")
os.makedirs(LESSONS_DOCS_DIR, exist_ok=True)

# Convertir cada archivo README.md a HTML
def convert_md_to_html(md_file, html_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Agregar estructura HTML básica
    html_full = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Curso de Django - Lección</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <link rel="stylesheet" href="../css/styles.css">
        <style>
            .lesson-content {{
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
                background: white;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            .lesson-content h1, .lesson-content h2, .lesson-content h3 {{
                color: #667eea;
            }}
            .lesson-content a {{
                color: #667eea;
                text-decoration: none;
            }}
            .lesson-content a:hover {{
                text-decoration: underline;
            }}
            .lesson-content pre {{
                background: #f5f5f5;
                padding: 1rem;
                border-radius: 4px;
                overflow-x: auto;
            }}
            .lesson-content code {{
                background: #f5f5f5;
                padding: 0.2rem 0.4rem;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        <header>
            <img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" alt="Django Logo" class="django-logo">
            <h1>Curso de Django 🚀</h1>
            <p>Aprende Django desde cero con Iroennys Dev</p>
        </header>
        <div class="container">
            <div class="lesson-content">
                {html_content}
            </div>
        </div>
        <footer>
            <p>Creador: <a href="https://github.com/iroennys-admin" target="_blank">Iroennys Dev</a> | © 2023 Curso de Django</p>
        </footer>
    </body>
    </html>
    """
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_full)

# Recorrer las lecciones y convertir cada README.md
def convert_lessons():
    for lesson_dir in os.listdir(LESSONS_DIR):
        lesson_path = os.path.join(LESSONS_DIR, lesson_dir)
        if os.path.isdir(lesson_path):
            md_file = os.path.join(lesson_path, "README.md")
            if os.path.exists(md_file):
                html_file = os.path.join(LESSONS_DOCS_DIR, f"{lesson_dir}.html")
                convert_md_to_html(md_file, html_file)
                print(f"Convertido: {md_file} -> {html_file}")

if __name__ == "__main__":
    convert_lessons()