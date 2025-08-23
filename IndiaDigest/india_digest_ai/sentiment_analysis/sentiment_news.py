import pandas as pd
import os
from .sentiment import get_sentiment

def analyze_news_articles(file_path):
    df = pd.read_csv(file_path)

    if 'title' not in df.columns or 'summary' not in df.columns:
        print(f"[!] Required columns missing in {file_path}")
        return

    # Apply sentiment to both title and summary
    df['title_sentiment'] = df['title'].apply(get_sentiment)
    df['summary_sentiment'] = df['summary'].apply(get_sentiment)

    # Save new file
    output_path = file_path.replace(".csv", "_sentiment.csv")
    df.to_csv(output_path, index=False)
    print(f"[✔] Sentiment added for Google News and saved to {output_path}")
