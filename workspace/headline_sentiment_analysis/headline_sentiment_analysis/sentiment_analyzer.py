from nltk.sentiment import SentimentIntensityAnalyzer
from typing import Dict

class SentimentAnalyzer:
    def __init__(self, headline: str):
        self.headline = headline
        self.sentiment_scores = None

    def analyze_sentiment(self) -> Dict[str, float]:
        sia = SentimentIntensityAnalyzer()
        self.sentiment_scores = sia.polarity_scores(self.headline)
        return self.sentiment_scores
