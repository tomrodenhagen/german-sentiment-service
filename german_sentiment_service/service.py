class SentimentService:
    def __init__(self, model):
        self.model = model

    def get_sentiment(self, texts):
        return self.model.predict_sentiment(texts)