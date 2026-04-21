# Complaint Analysis System

A production-ready NLP system for analyzing customer complaints.

Features:

- User authentication
- Complaint classification
- Sentiment analysis
- Keyword extraction
- Priority detection
- Dashboard analytics

INSTALLATION:

pip install -r requirements.txt

python -m spacy download en_core_web_sm

python model.py

python app.py

Open:

http://127.0.0.1:5000

DEPLOYMENT ON RENDER:

1. Push code to GitHub
2. Create new Web Service
3. Add build command:

pip install -r requirements.txt

4. Start command:

python app.py