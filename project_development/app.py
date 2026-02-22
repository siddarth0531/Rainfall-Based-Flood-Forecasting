from flask import Flask, render_template, request
import numpy as np
from joblib import load

app = Flask(__name__)

# Load the brain (model) and the translator (scaler)
model = load('floods.save')
scaler = load('transform.save')

@app.route('/')
def home():
    return render_template('home.html') # This is your landing page

@app.route('/predict_form')
def predict_form():
    return render_template('index.html') # This is your input form

@app.route('/predict', methods=['POST'])
def predict():
    # Collect data from the 5 input fields
    try:
        # We use a list comprehension to get f1 through f5
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        
        # Scale the data using our saved 'translator'
        scaled_features = scaler.transform(final_features)
        
        # Make the prediction
        prediction = model.predict(scaled_features)

        # SWAP THESE TO TEST
        if prediction == 0:  # Changed from 1 to 0
            return render_template('chance.html')
        else:
            return render_template('no chance.html')
            
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)