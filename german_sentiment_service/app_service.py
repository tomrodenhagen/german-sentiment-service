from app import sentiment_model
from service import SentimentService
from fastapi import Depends


async def get_sentiment_service():
    return SentimentService(sentiment_model)
