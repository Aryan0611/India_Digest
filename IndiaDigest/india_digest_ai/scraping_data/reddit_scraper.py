import praw
import pandas as pd
from datetime import datetime
import os
from config import REDDIT


def get_reddit_client():
    reddit = praw.Reddit(
        client_id=REDDIT["client_id"],
        client_secret=REDDIT["client_secret"],
        user_agent=REDDIT["user_agent"],
        username=REDDIT["username"],
        password=REDDIT["password"]
    )
    return reddit

def scrape_reddit_posts(keyword="India", subreddit="india", limit=20):
    reddit = get_reddit_client()
    posts = []

    for post in reddit.subreddit(subreddit).search(keyword, sort="top", limit=limit):
        posts.append({
            "id": post.id,
            "title": post.title,
            "score": post.score,
            "url": post.url,
            "num_comments": post.num_comments,
            "created": datetime.fromtimestamp(post.created),
            "subreddit": subreddit
        })

    df = pd.DataFrame(posts)

    # Save to data/
    os.makedirs("data", exist_ok=True)
    filename = f"reddit_{keyword.replace(' ', '_')}_{datetime.today().date()}.csv"
    filepath = os.path.join("data", filename)
    df.to_csv(filepath, index=False)
    print(f"[✔] Saved {len(df)} Reddit posts for '{keyword}' to {filepath}")
    return filepath
