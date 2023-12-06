from flask import Flask, jsonify, request, send_from_directory, render_template, redirect, url_for
import os
import utilities as util

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

#------------Compresor de vídeo--------------------
@app.route('/compresor_video', methods=['GET', 'POST'])
def compresor_video():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            compressed_filename = util.upload_to_server(file, 0, "mp4")
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
            word_filename = util.upload_to_server(file, 1, "word")
            if word_filename:
                file_url = url_for('uploaded_file', filename=word_filename)
                return jsonify({'fileUrl': file_url})
    return render_template('pdf_word.html')

#------------Jpg a Webp--------------------
@app.route('/jpg_a_webp', methods=['GET', 'POST'])
def jpg_a_webp():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            webp_filename = util.upload_to_server(file, 2, "webp")
            if webp_filename:
                file_url = url_for('uploaded_file', filename=webp_filename)
                return jsonify({'fileUrl': file_url})
    return render_template('jpg_webp.html')

#------------Jpg a png--------------------
@app.route('/jpg_a_png', methods=['GET', 'POST'])
def jpg_a_png():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            png_filename = util.upload_to_server(file, 3, "png")
            if png_filename:
                file_url = url_for('uploaded_file', filename=png_filename)
                return jsonify({'fileUrl': file_url})
    return render_template('jpg_png.html')

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
