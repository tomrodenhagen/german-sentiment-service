from fastapi import APIRouter, Depends
from service import SentimentService
from app_service import get_sentiment_service

api_router = APIRouter()


@api_router.post('/', status_code=201)
async def get_sentiment(sentiment_service: SentimentService = Depends(get_sentiment_service)):
   # texts = payload.dict()
  #  result = sentiment_service.get_sentiment(texts)

    return {'result': "SENTIMENT"}