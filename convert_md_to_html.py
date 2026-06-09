#!/usr/bin/env python3

import os
import markdown

# Directorios
LESSONS_DIR = "lecciones"
DOCS_DIR = "docs"
TEMPLATES_DIR = "templates"

# Crear directorios necesarios
LESSONS_DOCS_DIR = os.path.join(DOCS_DIR, "lecciones")
os.makedirs(LESSONS_DOCS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# Convertir Markdown a HTML con plantilla
def convert_md_to_html(md_file, html_file, template_file="templates/base.html"):
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Usar plantilla base si existe
    if os.path.exists(template_file):
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()
        html_full = template.replace('{% block content %}{% endblock %}', html_content)
    else:
        # Plantilla básica si no existe
        html_full = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Curso de Django - Lección</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="/static/css/styles.css">
        </head>
        <body>
            <div class="container py-5">
                <div class="lesson-content">
                    {html_content}
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        """
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_full)

# Convertir lecciones individuales
def convert_lessons():
    for lesson_dir in sorted(os.listdir(LESSONS_DIR)):
        lesson_path = os.path.join(LESSONS_DIR, lesson_dir)
        if os.path.isdir(lesson_path):
            md_file = os.path.join(lesson_path, "README.md")
            if os.path.exists(md_file):
                html_file = os.path.join(LESSONS_DOCS_DIR, f"{lesson_dir}.html")
                convert_md_to_html(md_file, html_file)
                print(f"Convertido: {md_file} -> {html_file}")

# Convertir página principal
def convert_index():
    if os.path.exists("curso_django.md"):
        convert_md_to_html("curso_django.md", os.path.join(DOCS_DIR, "index.html"), "templates/index.html")
        print(f"Convertido: curso_django.md -> docs/index.html")

if __name__ == "__main__":
    convert_index()
    convert_lessons()