## headline_extractor.py

from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


class BaseNewsDomain(ABC):
    def __init__(self, url: str):
        self.url = url
        self.headlines = []

    @abstractmethod
    def extract_headlines(self) -> list:
        pass

    def _get_page_content(self) -> BeautifulSoup:
        response = requests.get(self.url)
        return BeautifulSoup(response.text, 'html.parser')
