# app.py
import streamlit as st
from utils import detect_emotion, suggest_quote

st.set_page_config(page_title="Moodifier - Mental Health Journal", layout="centered")

st.title("🧠 Moodifier: Not just a journal... but your support system!")
st.markdown("Write your thoughts, and let us help you understand your emotions.")

# Text area for journal entry
text = st.text_area("📓 What's on your mind today?", height=200)

# Analyze button
if st.button("🧠 Analyze My Mood"):
    if not text.strip():
        st.warning("Please write something before analyzing.")
    else:
        with st.spinner("Analyzing your mood..."):
            emotion, confidence = detect_emotion(text)

        st.subheader("🧾 Analysis Result")
        st.write(f"**Detected Emotion:** `{emotion}`")
        st.write(f"**Confidence:** `{round(confidence * 100)}%`")

        st.subheader("🌈 Suggested Thought")
        st.success(suggest_quote(emotion))

        st.markdown("---")
        st.caption("This is an AI tool and not a substitute for professional help.")
