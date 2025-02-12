from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/app_success_model.pkl")

model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint to predict app success."""
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"success_prediction": int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)