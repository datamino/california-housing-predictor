from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os
import numpy as np
import json

app = Flask(__name__)


MODEL_PATH = 'models/house_price_predictor.pkl'

def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except:
        return None

model = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    
    input_df = pd.DataFrame({
        'longitude': [float(data['longitude'])],
        'latitude': [float(data['latitude'])],
        'housing_median_age': [int(data['housing_median_age'])],
        'total_rooms': [int(data['total_rooms'])],
        'total_bedrooms': [int(data['total_bedrooms'])],
        'population': [int(data['population'])],
        'households': [int(data['households'])],
        'median_income': [float(data['median_income'])],
        'ocean_proximity': [data['ocean_proximity']]
    })
    
  
    if model is not None:
        try:
            prediction = model.predict(input_df)[0]
            return jsonify({
                'status': 'success',
                'prediction': float(prediction),
                'formatted_prediction': f"${prediction:,.2f}"
            })
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            })
    else:
        # Placeholder prediction for demonstration
        fake_prediction = 350000 + (float(data['median_income']) * 50000) - (float(data['longitude']) * 10000) + (float(data['latitude']) * 5000)
        if data['ocean_proximity'] == 'INLAND':
            fake_prediction *= 0.8
        else:
            fake_prediction *= 1.2
            
        return jsonify({
            'status': 'demo',
            'prediction': float(fake_prediction),
            'formatted_prediction': f"${fake_prediction:,.2f}"
        })

@app.route('/example_data', methods=['GET'])
def example_data():
   
    np.random.seed(42)
    n = 200
    example_data = {
        'locations': [{
            'longitude': float(lon),
            'latitude': float(lat),
            'value': float(val)
        } for lon, lat, val in zip(
            np.random.uniform(-124, -114, n),
            np.random.uniform(32.5, 42, n),
            np.random.uniform(30000, 1000000, n)
        )],
        'proximities': [{
            'proximity': prox,
            'values': [float(v) for v in np.random.uniform(30000, 1000000, 10)]
        } for prox in ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND']],
        'correlation': {
            'features': ['Age', 'Rooms', 'Bedrooms', 'Population', 'Households', 'Income', 'Value'],
            'values': [[float(v) for v in row] for row in np.random.uniform(-1, 1, (7, 7))]
        }
    }
    
   
    for i in range(7):
        example_data['correlation']['values'][i][i] = 1.0
        for j in range(i+1, 7):
            example_data['correlation']['values'][j][i] = example_data['correlation']['values'][i][j]
    
    return jsonify(example_data)

if __name__ == '__main__':
    app.run()