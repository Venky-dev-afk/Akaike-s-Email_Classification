# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import string
import nltk
import joblib
nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv('dataset/combined_emails_with_natural_pii.csv')

# Clean text
def clean_text(text):
    text = text.lower()
    text = ''.join([ch for ch in text if ch not in string.punctuation])
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

df['clean_email'] = df['email'].apply(clean_text)

# Prepare features and labels
X = df['clean_email']
y = df['type']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model training
clf = LogisticRegression()
clf.fit(X_train_vec, y_train)

# Evaluation
y_pred = clf.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# Save model & vectorizer
joblib.dump(clf, 'model/email_classifier.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')
