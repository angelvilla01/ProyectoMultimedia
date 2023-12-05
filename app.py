from flask import Flask, jsonify, request, send_from_directory, render_template, redirect, url_for
import os
from reportlab.lib.pagesizes import letter 
from reportlab.pdfgen import canvas 
from PIL import Image

import utilities as util

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #return send_from_directory(UPLOAD_FOLDER, filename) (con esto veríamos el fichero)
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True) #descarga..

#------------Compresor de vídeo--------------------
@app.route('/compresor_video', methods=['GET', 'POST'])
def compresor_video():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            compressed_filename = util.upload_to_server(file, 0)
            if compressed_filename:
                file_url = url_for('uploaded_file', filename=compressed_filename)
                return jsonify({'fileUrl': file_url})
    return render_template('compresor_video.html')

#------------PDF A WORD--------------------
@app.route('/pdf_a_word', methods=['GET', 'POST'])
def pdf_a_word():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            word_filename = util.upload_to_server(file, 1)
            if word_filename:
                file_url = url_for('uploaded_file', filename=word_filename)
                return jsonify({'fileUrl': file_url})
    return render_template('pdf_word.html')

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
