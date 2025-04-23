from flask import Flask, request, jsonify
from utils import mask_pii
from models import predict_email_type

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Email Classification API is running!'
    
@app.route('/classify', methods=['POST'])
def classify_email():
    data = request.json
    email_text = data.get('email', '')

    if not email_text:
        return jsonify({'error': 'No email provided'}), 400

    # Step 1: Mask PII
    masked_email, pii_entities = mask_pii(email_text)

    # Step 2: Predict category
    prediction = predict_email_type(masked_email)

    return jsonify({
        'masked_email': masked_email,
        'entities': pii_entities,
        'category': prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
