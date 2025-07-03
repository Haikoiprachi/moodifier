from transformers import pipeline
emotion_classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-emotion", top_k=1)

quotes = {
    "joy": "Keep smiling and let your inner light shine.",
    "sadness": "It's okay to feel down. Brighter days are coming.",
    "anger": "Take a deep breath. Let go of what you can't control.",
    "fear": "You are stronger than your fears.",
    "love": "Let love guide your way.",
    "surprise": "Embrace the unexpected. Life is full of wonder."
}

def detect_emotion(text):
    result = emotion_classifier(text)[0]
    return result[0]['label'], result[0]['score']

def suggest_quote(emotion):
    return quotes.get(emotion.lower(), "Every emotion is valid. Take your time to understand it.")
