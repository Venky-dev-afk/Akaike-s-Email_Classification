# Email Classification System with PII Masking

This project is an end-to-end solution that:
- Masks Personally Identifiable Information (PII) such as names, emails, phone numbers, and Aadhar numbers.
- Classifies the email into predefined categories like **Incident**, **Request**, **Change**, and **Problem** using a trained ML model.
- Exposes this functionality through a Flask-based REST API.
- Returns structured output in JSON format.

---

## Project Structure

email-classification-api/ │ 
├── app.py # Flask API 
├── model_training.py # Script to train and evaluate the ML model 
├── test.py # Script to test the deployed API 
├── utils.py # Utility functions: PII masking and preprocessing 
├── model/ │ 
  ├── email_classifier.pkl # Trained classifier 
  │ └── vectorizer.pkl # TF-IDF vectorizer 
├── data/ 
  │ └── emails.csv # Dataset with 'email' and 'type' columns 
└── README.md

## Requirements

Install the required packages using:

bash - 
pip install -r requirements.txt

Also, make sure to download NLTK stopwords

## How to Run the Project:

1. Clone the Repository
2. Train the Model (optional, already trained model is provided)
3. Run the Flask API (python app.py) - You should see: Email Classification API is running!
4. Test the API - (you can use the provided test.py script to test the api)


## API Details: 

Endpoint
POST /classify

Request Body
{
  "email": "Hi, my name is Alice Smith. My email is alice.smith@example.com ..."
}

Response
masked_email: The input with PII replaced.

entities: List of detected PII with classification and position.

category: Predicted email type.
