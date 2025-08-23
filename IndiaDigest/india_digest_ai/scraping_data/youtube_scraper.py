import pandas as pd
from datetime import datetime
import os
from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

def get_youtube_service():
    return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_videos(service, query, max_results=5):
    request = service.search().list(
        part='snippet',
        q=query,
        maxResults=max_results,
        type='video',
        relevanceLanguage='en',
        regionCode='IN'
    )
    response = request.execute()
    # ✅ Only keep results that contain videoId
    video_ids = []
    for item in response.get('items', []):
        if 'videoId' in item.get('id', {}):
            video_ids.append(item['id']['videoId'])

    return video_ids

def fetch_comments(service, video_id, max_comments=20):
    comments = []

    try:
        request = service.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=min(max_comments, 100),
            textFormat='plainText'
        )
        response = request.execute()

        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append({
                "video_id": video_id,
                "author": comment['authorDisplayName'],
                "comment": comment['textDisplay'],
                "published_at": comment['publishedAt'],
                "like_count": comment['likeCount']
            })

    except Exception as e:
        print(f"[⚠️] Skipped video {video_id} — Reason: {e}")

    return comments

def scrape_youtube_comments(topic="Lok Sabha Election", max_videos=3, comments_per_video=20):
    service = get_youtube_service()
    video_ids = search_videos(service, topic, max_results=max_videos)

    all_comments = []
    for vid in video_ids:
        video_comments = fetch_comments(service, vid, max_comments=comments_per_video)
        if video_comments:
            all_comments.extend(video_comments)
        else:
            print(f"[ℹ️] No comments found or video skipped: {vid}")

    df = pd.DataFrame(all_comments)

    # Save to CSV
    os.makedirs("data", exist_ok=True)
    filename = f"youtube_{topic.replace(' ', '_')}_{datetime.today().date()}.csv"
    filepath = os.path.join("data", filename)
    df.to_csv(filepath, index=False)
    print(f"[✔] Saved {len(df)} YouTube comments to {filepath}")
    return filepath
