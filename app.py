from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfReader

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        try:
            reader = PdfReader(filepath)
            num_pages = len(reader.pages)
        except Exception:
            os.remove(filepath)
            return jsonify({'error': 'Failed to read PDF'}), 400
        os.remove(filepath)
        return jsonify({'filename': filename, 'num_pages': num_pages})
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num_pages = data.get('num_pages')
    color_pages = data.get('color_pages')
    bw_pages = data.get('bw_pages')
    if not all(isinstance(x, int) and x >= 0 for x in [num_pages, color_pages, bw_pages]):
        return jsonify({'error': 'Invalid input'}), 400
    if color_pages + bw_pages != num_pages:
        return jsonify({'error': 'Page count mismatch'}), 400
    bw_cost = bw_pages * 4
    color_cost = color_pages * 6
    total = bw_cost + color_cost
    return jsonify({
        'num_pages': num_pages,
        'bw_pages': bw_pages,
        'color_pages': color_pages,
        'bw_cost': bw_cost,
        'color_cost': color_cost,
        'total': total
    })

if __name__ == '__main__':
    app.run(debug=True) 