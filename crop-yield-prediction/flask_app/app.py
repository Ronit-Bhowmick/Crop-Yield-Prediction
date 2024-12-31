from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the model and scaler
model = joblib.load('../crop_yield_prediction_model.pkl')
scaler = joblib.load('../scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the form
    rainfall = float(request.form['rainfall'])
    soil_quality = float(request.form['soilQuality'])
    farm_size = float(request.form['farmSize'])
    sunlight_hours = float(request.form['sunlightHours'])
    fertilizer = float(request.form['fertilizer'])

    # Create a numpy array from the input data
    input_data = np.array([[rainfall, soil_quality, farm_size, sunlight_hours, fertilizer]])

    # Transform the input data using the scaler
    input_data_scaled = scaler.transform(input_data)

    # Make prediction using the model
    prediction = model.predict(input_data_scaled)

    # Render the template with the prediction result
    return render_template('index.html', prediction_text=f'Predicted Yield: {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True)