import feedparser
import pandas as pd
from datetime import datetime
import os

def scrape_google_news_rss(keyword="India", max_articles=10):
    """
    Scrape news articles from Google News RSS based on a keyword.

    Args:
        keyword (str): The topic to search news for.
        max_articles (int): Number of articles to fetch.

    Returns:
        str: File path of the saved CSV.
    """

    # Step 1: Create RSS feed URL (specific to India news)
    feed_url = f"https://news.google.com/rss/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN:en"

    # Step 2: Parse RSS feed
    feed = feedparser.parse(feed_url)

    # Step 3: Extract data into list of dictionaries
    articles = []
    for entry in feed.entries[:max_articles]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        })

    # Step 4: Convert to DataFrame
    df = pd.DataFrame(articles)

    # Step 5: Save CSV to /data/ folder
    today = datetime.today().strftime("%Y-%m-%d")
    filename = f"news_{keyword.replace(' ', '_')}_{today}.csv"
    filepath = os.path.join("data", filename)

    os.makedirs("data", exist_ok=True)  # ensure the folder exists
    df.to_csv(filepath, index=False)

    print(f"[✔] Scraped {len(df)} articles on '{keyword}' and saved to: {filepath}")
    return filepath
