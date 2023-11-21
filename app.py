from flask import Flask, request, send_from_directory, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
import subprocess
from pdf2docx import Converter
from reportlab.lib.pagesizes import letter 
from reportlab.pdfgen import canvas 
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'flv', 'mkv', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

#------------Compresor de vídeo--------------------
@app.route('/compresor_video', methods=['GET', 'POST'])
def compresor_video():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            compressed_filename = compress_video(filename)
            return send_from_directory(app.config['UPLOAD_FOLDER'], compressed_filename, as_attachment=True)
    return render_template('compresor_video.html')

def compress_video(filename):
    compressed_filename = f"compressed_{filename}"
    ruta_intermedia = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

    input_path = os.path.join( ruta_intermedia, filename)
    output_path = os.path.join( ruta_intermedia, compressed_filename)

    result = subprocess.call(['ffmpeg', '-i', input_path, '-vf', 'scale=640:360', '-b:v', '500k', '-vcodec', 'libx264', '-acodec', 'aac', output_path])
    return compressed_filename

#------------PDF A WORD--------------------
@app.route('/pdf_a_word', methods=['GET', 'POST'])
def pdf_a_word():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            print(filename)
            
            word_filename = pdf_to_word(filename)
            return send_from_directory(app.config['UPLOAD_FOLDER'], word_filename, as_attachment=True)
    return render_template('pdf_word.html')


def pdf_to_word(filename):
    word_filename = f"word_{filename.removesuffix('.pdf')}.docx"
    ruta_intermedia = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

    input_path = os.path.join( ruta_intermedia, filename)
    output_path = os.path.join( ruta_intermedia, word_filename)

    cv = Converter(input_path)
    cv.convert(output_path, start=0, end=None)

    cv.close()
    return word_filename

#------------JPG a PDF--------------------
def jpg_to_pdf(jpg_paths, output_path): 
    c = canvas.Canvas(output_path, pagesize=letter) 
 
    for jpg_path in jpg_paths: 
        img = Image.open(jpg_path) 
        width, height = letter 
        img_width, img_height = img.size 
 
        # Ajustar la imagen al tamaño de la página 
        aspect_ratio = img_width / img_height 
        if img_width > img_height: 
            img_width = width 
            img_height = width / aspect_ratio 
        else: 
            img_height = height 
            img_width = height * aspect_ratio 
 
        c.drawImage(jpg_path, 0, 0, width=img_width, height=img_height) 
        c.showPage() 
 
    c.save()

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
