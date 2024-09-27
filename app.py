# app.py
from flask import Flask, request, render_template
import os
from process_image import extract_text_from_image, summarize_text

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Extract text and summarize
        extracted_text = extract_text_from_image(image_path)
        summary = summarize_text(extracted_text)

        return f"<h2>Summary:</h2><p>{summary}</p>"
    else:
        return 'File upload failed'

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
