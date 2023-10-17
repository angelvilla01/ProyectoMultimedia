from flask import Flask, request, send_from_directory, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'flv', 'mkv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'video' not in request.files:
            return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            compressed_filename = compress_video(filename)
            return send_from_directory(app.config['UPLOAD_FOLDER'], compressed_filename, as_attachment=True)
    return '''
    <!doctype html>
    <title>Upload Video</title>
    <h1>Upload Video</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=video>
      <input type=submit value=Upload>
    </form>
    '''

def compress_video(filename):
    compressed_filename = f"compressed_{filename}"
    ruta_intermedia = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])

    input_path = os.path.join( ruta_intermedia, filename)
    output_path = os.path.join( ruta_intermedia, compressed_filename)

    print("Entrada -> "+input_path)
    print("Salida -> "+output_path)
    result = subprocess.call(['ffmpeg', '-i', input_path, '-vf', 'scale=640:360', '-b:v', '500k', '-vcodec', 'libx264', '-acodec', 'aac', output_path])
    return compressed_filename

@app.route('/')
def index():
    return redirect(url_for('upload'))

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
