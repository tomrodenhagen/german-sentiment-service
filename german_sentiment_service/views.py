from fastapi import APIRouter, Depends
from service import SentimentService
from app_service import get_sentiment_service

api_router = APIRouter()

@api_router.post('/', status_code=201)
async def get_sentiment(text :str , sentiment_service: SentimentService = Depends(get_sentiment_service)):
    result = sentiment_service.get_sentiment(text)
    return {'sentiment': result}