## dom_parser.py

from bs4 import BeautifulSoup
from typing import List

class DOMParser:
    def __init__(self, html: str):
        self.html = html

    def extract_headlines(self) -> List[str]:
        soup = BeautifulSoup(self.html, 'html.parser')
        headlines = soup.find_all('h1')
        return [headline.text for headline in headlines]
