import streamlit as st
from transformers import pipeline

# Load the pretrained emotion detection model
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

emotion_classifier = load_model()

# Streamlit UI
st.set_page_config(page_title="Moodifier – Emotion Detector", page_icon="🌈", layout="centered")

st.title("🌈 Moodifier – Your Emotion Detector")
st.write("Type your thoughts below, and I'll tell you how you might be feeling.")

# User input
text = st.text_area("What's on your mind today?", "")

if st.button("Detect Emotion"):
    if text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Analyzing your emotions..."):
            result = emotion_classifier(text)[0]
            emotion = result['label']
            confidence = result['score']

        # Show results
        st.success(f"**Detected Emotion:** {emotion}")
        st.write(f"**Confidence:** {confidence:.2%}")
