import pandas as pd
import os
from .sentiment import get_sentiment

def analyze_youtube_comments(file_path):
    df = pd.read_csv(file_path)
    if 'comment' not in df.columns:
        print(f"[!] No 'comment' column in {file_path}")
        return

    df['sentiment'] = df['comment'].apply(get_sentiment)

    # Save new CSV
    output_path = file_path.replace(".csv", "_sentiment.csv")
    df.to_csv(output_path, index=False)
    print(f"[✔] Sentiment added and saved to {output_path}")
