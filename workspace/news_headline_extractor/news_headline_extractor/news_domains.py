from headline_extractor import BaseNewsDomain


class CNNNewsDomain(BaseNewsDomain):
    def __init__(self, url: str = 'https://www.cnn.com'):
        super().__init__(url)

    def extract_headlines(self) -> list:
        soup = self._get_page_content()
        headlines = soup.find_all('h3', class_='cd__headline')
        return [headline.text for headline in headlines]


class FoxNewsDomain(BaseNewsDomain):
    def __init__(self, url: str = 'https://www.foxnews.com'):
        super().__init__(url)

    def extract_headlines(self) -> list:
        soup = self._get_page_content()
        headlines = soup.find_all('h2', class_='title')
        return [headline.text for headline in headlines]


class BBCNewsDomain(BaseNewsDomain):
    def __init__(self, url: str = 'https://www.bbc.com/news'):
        super().__init__(url)

    def extract_headlines(self) -> list:
        soup = self._get_page_content()
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        return [headline.text for headline in headlines]
