import joblib
import os

# Paths to saved model and vectorizer
MODEL_PATH = os.path.join('model', 'email_classifier.pkl')
VECTORIZER_PATH = os.path.join('model', 'vectorizer.pkl')

# Load model and vectorizer
classifier = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Function to predict category from email text
def predict_email_type(email_text):
    vectorized_input = vectorizer.transform([email_text])
    predicted_class = classifier.predict(vectorized_input)[0]
    return predicted_class
