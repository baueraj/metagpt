## main.py
import requests
from typing import Dict, List
from dom_parser import DOMParser
from sentiment_analyzer import SentimentAnalyzer

class Main:
    def __init__(self, url: str):
        self.url = url
        self.html = self.fetch_html()
        self.dom_parser = DOMParser(self.html)
        self.sentiment_analyzer = SentimentAnalyzer()

    def fetch_html(self) -> str:
        response = requests.get(self.url)
        return response.text

    def hide_negative_headlines(self) -> None:
        headlines = self.dom_parser.extract_headlines()
        for headline in headlines:
            self.sentiment_analyzer.headline = headline
            sentiment_scores = self.sentiment_analyzer.analyze_sentiment()
            if sentiment_scores['compound'] < 0:
                # Hide the headline
                print(f"Hidden headline: {headline}")

if __name__ == "__main__":
    main = Main("https://www.example.com")
    main.hide_negative_headlines()
