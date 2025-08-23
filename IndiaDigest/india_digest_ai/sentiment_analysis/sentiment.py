from textblob import TextBlob

def get_sentiment(text):
    """
    Classify sentiment using TextBlob polarity.
    Returns: 'Positive', 'Negative', 'Neutral'
    """
    if not text or not isinstance(text, str):
        return 'Neutral'

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'
