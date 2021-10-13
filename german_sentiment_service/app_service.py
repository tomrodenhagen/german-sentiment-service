from german_sentiment_service.app import sentiment_model
from german_sentiment_service.service import SentimentService

async def get_sentiment_service():
    return SentimentService(sentiment_model)
