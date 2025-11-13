# utils.py
from transformers import pipeline

# --- Cache the model so it's loaded only once ---
_model = None

def load_model():
    global _model
    if _model is None:
        _model = pipeline(
            "text-classification",
            model="cardiffnlp/twitter-roberta-base-emotion",
            top_k=1
        )
    return _model


quotes = {
    "joy": "Keep smiling and let your inner light shine.",
    "sadness": "It's okay to feel down. Brighter days are coming.",
    "anger": "Take a deep breath. Let go of what you can't control.",
    "fear": "You are stronger than your fears.",
    "love": "Let love guide your way.",
    "surprise": "Embrace the unexpected. Life is full of wonder."
}


def detect_emotion(text):
    """
    Detects emotion from text using the Hugging Face model.
    Returns (emotion, confidence).
    """
    model = load_model()
    result = model(text)

    # Handle both possible output formats
    if isinstance(result, list) and len(result) > 0:
        first = result[0]
        if isinstance(first, list) and len(first) > 0:
            r = first[0]
        elif isinstance(first, dict):
            r = first
        else:
            r = {"label": "unknown", "score": 0.0}
    elif isinstance(result, dict):
        r = result
    else:
        r = {"label": "unknown", "score": 0.0}

    label = r.get("label", "unknown")
    score = float(r.get("score", 0.0))
    return label, score


def suggest_quote(emotion):
    """Suggest a quote based on the detected emotion."""
    return quotes.get(emotion.lower(), "Every emotion is valid. Take your time to understand it.")

