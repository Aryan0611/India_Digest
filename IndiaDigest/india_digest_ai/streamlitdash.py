import streamlit as st
import pandas as pd
from genai.summarizer import summarize_news, analyze_sentiment, deep_dive, expert_commentary
from utils.visualizer import plot_sentiment_pie, generate_wordcloud
import os

# ---------- APP TITLE ----------
st.set_page_config(page_title="IndiaDigest", layout="wide")
st.title("🇮🇳 IndiaDigest - GenAI Powered Weekly Newsletter")

# ---------- INPUT ----------
topic = st.text_input("Enter a Topic:", "Lok Sabha Election")

# ---------- LOAD DATA ----------
news_file = f"data/news_{topic.replace(' ', '_')}_{pd.Timestamp.today().date()}.csv"
reddit_file = f"data/reddit_{topic.replace(' ', '_')}_{pd.Timestamp.today().date()}.csv"
youtube_file = f"data/youtube_{topic.replace(' ', '_')}_{pd.Timestamp.today().date()}.csv"

if os.path.exists(news_file) and os.path.exists(reddit_file) and os.path.exists(youtube_file):
    # ---------- GENAI SUMMARIES ----------
    st.header("📰 Weekly News Summary")
    st.write(summarize_news(news_file))

    st.header("💬 Public Sentiment (from YouTube)")
    st.write(analyze_sentiment(youtube_file, topic))

    st.header("🔍 Deep Dive of the Week")
    st.write(deep_dive(news_file, topic))

    st.header("🧑‍💼 Expert Commentary")
    st.write(expert_commentary(news_file, topic))

    # ---------- VISUALIZATIONS ----------
    st.subheader("📊 Sentiment Distribution")
    sentiment_scores = {"Positive": 40, "Negative": 35, "Neutral": 25}  # placeholder
    plot_sentiment_pie(sentiment_scores, topic, "data/sentiment_pie.png")
    st.image("data/sentiment_pie.png", caption="Public Sentiment Pie Chart")

    st.subheader("☁️ Word Cloud from Reddit Posts")
    df_reddit = pd.read_csv(reddit_file)
    generate_wordcloud(df_reddit["title"].tolist(), topic, "data/wordcloud.png")
    st.image("data/wordcloud.png", caption="Trending Words")
else:
    st.warning("⚠️ Please run the scrapers first to collect data for this topic.")
