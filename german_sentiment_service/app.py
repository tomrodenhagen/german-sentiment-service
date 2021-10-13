from fastapi import FastAPI, APIRouter
from germansentiment import SentimentModel

#We only want to load this once
sentiment_model = SentimentModel()

from views import api_router

app = FastAPI()
app.include_router(api_router)



