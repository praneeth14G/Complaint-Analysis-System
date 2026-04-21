import re
import spacy

nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text


def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            keywords.append(token.text)

    return ", ".join(keywords[:5])


def detect_priority(sentiment):
    if sentiment == "Negative":
        return "High"

    if sentiment == "Neutral":
        return "Medium"

    return "Low"