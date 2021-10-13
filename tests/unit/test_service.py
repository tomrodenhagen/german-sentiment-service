from german_sentiment_service.service import SentimentService

class mocked_sentiment_model:
    def predict_sentiment(self, dummy_input):
        return ["positive"]


def test_sentiment_service():
    mocked_model = mocked_sentiment_model()
    sentiment_service = SentimentService(mocked_model)
    res = sentiment_service.get_sentiment("")
    assert res=="positive"
