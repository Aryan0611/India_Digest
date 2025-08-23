'''from scraping_data.scraper import scrape_google_news_rss
from scraping_data.reddit_scraper import scrape_reddit_posts
from scraping_data.youtube_scraper import scrape_youtube_comments
if __name__ == "__main__":
    topics = [
        "Lok Sabha Election",
        "ISRO Mission",
        "Indian Budget",
        "Bollywood",
        "Stock Market"
    ]
    for topic in reddit_keywords:
       scrape_reddit_posts(keyword=topic, subreddit="india", limit=15)
    for topic in topics:
       scrape_google_news_rss(keyword=topic, max_articles=15)
    for topic in youtube_t:
        scrape_youtube_comments(topic=topic, max_videos=7, comments_per_video=15)'''

from sentiment_analysis.sentiment_reddit import analyze_reddit_posts
from sentiment_analysis.sentiment_youtube import analyze_youtube_comments
from sentiment_analysis.sentiment_news import analyze_news_articles

# Add actual file names below
analyze_reddit_posts("data/reddit_Lok_Sabha_Election_2025-07-28.csv")
analyze_youtube_comments("data/youtube_Lok_Sabha_Election_2025-07-28.csv")
analyze_news_articles("data/news_Lok_Sabha_Election_2025-07-28.csv")


