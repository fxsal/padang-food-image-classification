from flask import Flask, request, jsonify
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
import os
import json
from PIL import Image

app = Flask(__name__)

# Load model
model = load_model("model_padang_cnn.h5")

# Kelas
class_names = ['ayam_goreng', 'ayam_pop', 'daging_rendang', 'dendeng_batokok', 'gulai_ikan', 'gulai_tambusu', 'gulai_tunjang', 'telur_balado', 'telur_dadar']

# Load deskripsi makanan
with open("food_info.json", "r", encoding="utf-8") as f:
    food_info = json.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    img = img.resize((224, 224))
    x = img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)[0]
    idx = np.argmax(preds)
    confidence = float(preds[idx])
    label = class_names[idx]

    result = {
        "label": label if confidence >= 0.4 else "unknown",
        "confidence": confidence,
        "data": food_info.get(label, {
            "nama": "Tidak Dikenali",
            "deskripsi": "-",
            "sejarah": "-",
            "bahan": [],
            "sumber": "#"
        }) if confidence >= 0.4 else {
            "nama": "Gambar Tidak Dikenali",
            "deskripsi": "Model tidak yakin bahwa gambar tersebut adalah salah satu dari makanan khas Padang.",
            "sejarah": "-",
            "bahan": [],
            "sumber": "#"
        }
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))