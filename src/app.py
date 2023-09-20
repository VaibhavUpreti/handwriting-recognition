from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import cv2
# from htr_pipeline import read_page, DetectorConfig
from predict import get_img_text

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret_base_key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')

def home():
    return render_template('main.html')
@app.route('/', methods=['POST'])

def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # read_lines = predict(image_path)
        image_inst = cv2.imread(image_path)
        img,text=get_img_text(image_inst)
        flash('Successfull')
        return render_template('main.html', filename=filename, read_lines=text, image=img)
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)

def predict(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    read_lines = read_page(img, DetectorConfig(height=1000))
    return read_lines

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/ppt', methods=['GET'])
def ppt():
    return render_template('ppt.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
