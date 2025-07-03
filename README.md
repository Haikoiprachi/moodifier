## MOODIFIER = [MOOD + AMPLIFIER]

Moodifier is a journal writing platform which allows the user to write what they and thinking currently and according they get a feedback of how their current mood is. it is importat to track one's mental health that is why MOODIFIER helps to elevate and channelize your thought and help you to get better by suggesting good motivating quotes according to the user's mood.

oodifier uses a **pretrained transformer model** from Hugging Face to classify text into emotions. Behind the scenes:

1. Text is input via the Streamlit UI.
2. It is tokenized and passed through RoBERTa.
3. The most probable emotion is returned with its confidence score.
4. You see your predicted **mood** instantly!

## Run Locally

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/moodifier.git
cd moodifier
pip install -r requirements.txt
streamlit run app.py

##Future Scope
1-> Personalized Emotion Detection
Allow users to train Moodifier on their own data for more accurate, customized emotion predictions.

2-> Mood Tracking Over Time
Continuously monitor user mood and visualize trends through interactive graphs and dashboards.

3-> Mood Deterioration Alerts
Detect negative mood patterns over time and gently alert the user if emotional health is declining.

4-> Weekly Mood Reports
Auto-generate downloadable reports summarizing mood history, emotion distribution, and changes.
```
