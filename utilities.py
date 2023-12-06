from app import app
from werkzeug.utils import secure_filename
from pdf2docx import Converter
from PIL import Image
import os
import subprocess

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'flv', 'mkv', 'pdf', 'jpg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def compress_video(filename):
    compressed_filename = f"compressed_{filename}"
    ruta_intermedia = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

    input_path = os.path.join( ruta_intermedia, filename)
    output_path = os.path.join( ruta_intermedia, compressed_filename)

    result = subprocess.call(['ffmpeg', '-y', '-i', input_path, '-vf', 'scale=640:360', '-b:v', '500k', '-vcodec', 'libx264', '-acodec', 'aac', output_path])
    return compressed_filename


def pdf_to_word(filename):
    word_filename = f"word_{filename.removesuffix('.pdf')}.docx"
    ruta_intermedia = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

    input_path = os.path.join( ruta_intermedia, filename)
    output_path = os.path.join( ruta_intermedia, word_filename)

    cv = Converter(input_path)
    cv.convert(output_path, start=0, end=None)

    cv.close()
    return word_filename


def convert_file(filename, format):
    output_filename = f"{filename.removesuffix('.jpg')}."+ format
    ruta_intermedia = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

    input_path = os.path.join( ruta_intermedia, filename)
    output_path = os.path.join( ruta_intermedia, output_filename)

    imagen = Image.open(input_path)
    imagen.save(output_path, format)
    
    return output_filename


def upload_to_server(file, option, format):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        if option == 0:
            compressed_filename = compress_video(filename)
            return compressed_filename
        if option == 1:
            word_filename = pdf_to_word(filename)
            return word_filename
        if option == 2 or option == 3:
            out_filename = convert_file(filename,format)
            return out_filename
