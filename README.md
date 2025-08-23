# 📰 IndiaDigest: GenAI-Powered Weekly Newsletter

IndiaDigest is an **AI-powered news and social media analytics tool** that scrapes live data from **Google News, Reddit, and YouTube**, analyzes public sentiment, and generates **weekly digest summaries** using **GenAI (LangChain + LLMs)**.  
The project combines **Web Scraping**, **Python/Pandas**, and **Generative AI** to provide a unique perspective on **public opinion around current events**.

---

## 📸 Project Snapshot

<img width="1500" height="1024" alt="Image" src="https://github.com/user-attachments/assets/f8dc33cf-5d6c-4de7-963f-732445b330e2" />


---

## ✨ Features

- 🔍 **Web Scraping**
  - Google News (headlines + summaries)
  - Reddit Posts (topics, titles, metadata)
  - YouTube Comments (public opinion on trending videos)

- 📊 **Sentiment Analysis**
  - TextBlob for polarity (positive/neutral/negative)
  - GPT-powered contextual sentiment (via LangChain)

- 🧠 **AI-Powered Summaries**
  - LangChain + LLM integration
  - Generates concise weekly digest reports

- ☁️ **Cloud Integration (Optional)**
  - Store CSVs on **AWS S3**
  - Send digest updates via **AWS SNS**

- 📈 **Visualizations**
  - Sentiment distribution (pie & bar charts)
  - Trendline of positive/negative reactions over time

---

## 🛠️ Tech Stack

- **Programming**: Python 3.10+
- **Libraries**:  
  - Web scraping → `praw`, `google-api-python-client`, `newspaper3k`, `requests`, `BeautifulSoup4`
  - Data handling → `pandas`, `matplotlib`
  - Sentiment → `textblob`, `langchain`, `openai`
- **Cloud (Optional)**: AWS S3, AWS SNS
- **Frontend (Optional)**: Streamlit Dashboard

---

## 📂 Project Structure

```bash
india_digest_ai/
├── scraping_data/              # All scraping scripts
│   ├── reddit_scraper.py
│   ├── youtube_scraper.py
│   └── scraper.py              # Google News scraper
│
├── sentiment_analysis/         # Sentiment analysis scripts
│   ├── sentiment.py            # Core sentiment function
│   ├── sentiment_reddit.py
│   ├── sentiment_youtube.py
│   └── sentiment_news.py
│
├── data/                       # All CSVs stored here
├── config.py                   # API keys (Reddit, YouTube)
├── main.py                     # Pipeline runner
└── README.md

Scrapers → DataFrame → LangChain Summarizer
   ↓                  ↓
 Save CSV            Generate PDF
   ↓                  ↓
 Upload to S3 ←———→ Send SNS Alert
                          ↑
                        Scheduler (weekly)

