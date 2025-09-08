import pandas as pd
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# Initialize GPT model
llm = ChatOpenAI(model="gpt-4", temperature=0.5)

# ----------- PROMPT TEMPLATES -----------

# News Summarizer Prompt
news_prompt = PromptTemplate(
    input_variables=["articles"],
    template="""
    You are a professional journalist. Summarize the following news articles into
    4-5 bullet points focusing only on the most important developments.

    Articles:
    {articles}

    Summary:
    """
)

# Sentiment Analyzer Prompt
sentiment_prompt = PromptTemplate(
    input_variables=["comments", "topic"],
    template="""
    You are a political/social analyst. Analyze the following public comments about {topic}.
    Classify the overall sentiment as Positive, Negative, or Neutral.
    Then explain WHY in 3-4 sentences, citing common themes from the comments.

    Comments:
    {comments}

    Sentiment:
    """
)

# Deep Dive Prompt
deepdive_prompt = PromptTemplate(
    input_variables=["articles", "topic"],
    template="""
    Write a 'Deep Dive of the Week' article about {topic}.
    Use the following articles for context:
    {articles}

    Structure:
    - Background (why it matters)
    - Key events this week
    - Impact on politics/economy/society
    - What to watch next

    Keep it concise (200-300 words) but insightful.
    """
)

# Expert Commentary Prompt
expert_prompt = PromptTemplate(
    input_variables=["topic", "articles"],
    template="""
    Imagine you are a well-known news analyst writing a short opinion column.
    Based on the following articles about {topic}, provide expert commentary (150 words max).

    Articles:
    {articles}

    Commentary:
    """
)

# ----------- FUNCTIONS -----------

def summarize_news(news_csv):
    df = pd.read_csv(news_csv)
    articles_text = "\n".join(df["title"].head(5).tolist())
    chain = LLMChain(llm=llm, prompt=news_prompt)
    return chain.run(articles=articles_text)

def analyze_sentiment(comments_csv, topic):
    df = pd.read_csv(comments_csv)
    comments_text = "\n".join(df["comment"].head(20).astype(str).tolist())
    chain = LLMChain(llm=llm, prompt=sentiment_prompt)
    return chain.run(comments=comments_text, topic=topic)

def deep_dive(news_csv, topic):
    df = pd.read_csv(news_csv)
    articles_text = "\n".join(df["title"].head(8).tolist())
    chain = LLMChain(llm=llm, prompt=deepdive_prompt)
    return chain.run(articles=articles_text, topic=topic)

def expert_commentary(news_csv, topic):
    df = pd.read_csv(news_csv)
    articles_text = "\n".join(df["title"].head(5).tolist())
    chain = LLMChain(llm=llm, prompt=expert_prompt)
    return chain.run(topic=topic, articles=articles_text)
