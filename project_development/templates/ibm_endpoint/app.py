from flask import Flask, render_template, request
import requests

# NOTE: You will get these credentials from your IBM Cloud Console
API_KEY = "YOUR_IBM_API_KEY"
LOCATION = "us-south" # or your region
DEPLOYMENT_ID = "YOUR_DEPLOYMENT_ID"

app = Flask(__name__)

def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={API_KEY}"
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get Token
    iam_token = get_token()
    
    # 2. Prepare Data from Form
    feature_list = [float(x) for x in request.form.values()]
    
    # 3. IBM Payload Format
    payload_scoring = {
        "input_data": [{
            "fields": ["Rainfall", "Cloud_Cover", "Wet_Day_Freq", "Vapour_Pressure", "Temperature"],
            "values": [feature_list]
        }]
    }

    # 4. Call IBM Endpoint
    header = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + iam_token
    }
    endpoint = f"https://{LOCATION}.ml.cloud.ibm.com/ml/v4/deployments/{DEPLOYMENT_ID}/predictions?version=2021-05-01"
    
    response_scoring = requests.post(endpoint, json=payload_scoring, headers=header)
    result = response_scoring.json()
    
    # 5. Parse Prediction (0 or 1)
    prediction = result['predictions'][0]['values'][0][0]

    if prediction == 1:
        return render_template('chance.html')
    else:
        return render_template('no_chance.html')

if __name__ == "__main__":
    app.run(debug=True)