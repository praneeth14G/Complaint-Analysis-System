import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from textblob import TextBlob

import joblib


MODEL_FILE = "model.pkl"
VECTORIZER_FILE = "vectorizer.pkl"


def train_model():

    data = pd.read_csv("dataset/complaints.csv")

    X = data["text"]
    y = data["category"]

    vectorizer = TfidfVectorizer()

    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()

    model.fit(X_vec, y)

    joblib.dump(model, MODEL_FILE)
    joblib.dump(vectorizer, VECTORIZER_FILE)

    print("Model trained successfully")


def predict_category(text):

    model = joblib.load(MODEL_FILE)

    vectorizer = joblib.load(VECTORIZER_FILE)

    text_vec = vectorizer.transform([text])

    return model.predict(text_vec)[0]


def analyze_sentiment(text):

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"


if __name__ == "__main__":
    train_model()