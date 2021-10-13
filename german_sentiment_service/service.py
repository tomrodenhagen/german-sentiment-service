class SentimentService:
    def __init__(self, model):
        self.model = model

    def get_sentiment(self, text):
        batch = [text]
        return self.model.predict_sentiment(batch)[0]