from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploaded'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    if 'image' not in request.files:
        return redirect(url_for('index'))

    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Kirim ke backend
    with open(filepath, 'rb') as img:
        response = requests.post(
            "https://padang-api-525368436732.asia-southeast2.run.app/predict",
            files={"image": img}
        )
    
    result = response.json()
    return render_template('hasil.html', data=result["data"], confidence=result["confidence"], label=result["label"], filename=file.filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))