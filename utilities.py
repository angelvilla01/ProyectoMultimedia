from flask import Flask, request, send_from_directory, make_response, redirect, url_for
from app import app
from werkzeug.utils import secure_filename
import os
import subprocess

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'flv', 'mkv', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def compress_video(filename):
    compressed_filename = f"compressed_{filename}"
    ruta_intermedia = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

    input_path = os.path.join( ruta_intermedia, filename)
    output_path = os.path.join( ruta_intermedia, compressed_filename)

    result = subprocess.call(['ffmpeg', '-i', input_path, '-vf', 'scale=640:360', '-b:v', '500k', '-vcodec', 'libx264', '-acodec', 'aac', output_path])
    return compressed_filename

def upload_to_server(file,option):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        if option == 0:
            compressed_filename = compress_video(filename)
            return compressed_filename