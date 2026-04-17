import streamlit as st
import pandas as pd
import plotly.express as px
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

st.set_page_config(page_title="SentimentIQ", layout="wide")

st.title("🚀 SentimentIQ: Social Sentiment Intelligence System")

text = st.text_area("Enter your text here:")

def get_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score['compound']

    if compound >= 0.05:
        return "Positive", compound
    elif compound <= -0.05:
        return "Negative", compound
    else:
        return "Neutral", compound

def detect_topics(text):
    topics = {
        "Product": ["quality", "product", "item"],
        "Service": ["service", "support", "staff"],
        "Delivery": ["delivery", "shipping", "late"],
        "Pricing": ["price", "cost", "expensive", "cheap"]
    }

    result = {}

    for topic, keywords in topics.items():
        count = sum(word in text.lower() for word in keywords)
        result[topic] = count

    return result

if st.button("Analyze"):

    if not text.strip():
        st.warning("Please enter some text")
        st.stop()

    sentiment, score = get_sentiment(text)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Sentiment", sentiment)
    with col2:
        st.metric("Confidence", f"{score:.2f}")

    st.subheader("🔍 Topic Detection")

    topics = detect_topics(text)

    df = pd.DataFrame({
        "Topic": list(topics.keys()),
        "Frequency": list(topics.values())
    })

    fig = px.bar(df, x="Topic", y="Frequency")
    st.plotly_chart(fig)

    st.subheader("☁️ Word Cloud")

    wc = WordCloud().generate(text)

    fig_wc, ax = plt.subplots()
    ax.imshow(wc)
    ax.axis("off")

    st.pyplot(fig_wc)