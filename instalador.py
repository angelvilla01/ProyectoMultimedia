import subprocess
import sys

# Lista de bibliotecas a instalar
libraries = ["werkzeug", "pdf2docx", "flask", "reportlab", "pillow"]

# Función para instalar cada biblioteca
def install(library):
    subprocess.check_call([sys.executable, "-m", "pip", "install", library])

# Instalar todas las bibliotecas de la lista
for lib in libraries:
    install(lib)