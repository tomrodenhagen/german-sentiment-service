from fastapi import FastAPI, APIRouter
from germansentiment import SentimentModel

sentiment_model = SentimentModel()

from views import api_router

app = FastAPI()
app.include_router(api_router)



