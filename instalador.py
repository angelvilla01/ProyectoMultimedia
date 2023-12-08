import subprocess
import sys

# Lista de bibliotecas a instalar
libraries = ["flask", "werkzeug", "pdf2docx", "Pillow"]

# Función para instalar cada biblioteca
def install(library):
    subprocess.check_call([sys.executable, "-m", "pip", "install", library])

# Instalar todas las bibliotecas de la lista
for lib in libraries:
    install(lib)