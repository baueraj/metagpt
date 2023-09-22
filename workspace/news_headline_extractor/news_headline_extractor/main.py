## main.py
from news_domains import CNNNewsDomain, FoxNewsDomain, BBCNewsDomain


def main():
    news_domains = {
        "CNN": CNNNewsDomain(),
        "Fox": FoxNewsDomain(),
        "BBC": BBCNewsDomain()
    }

    for name, domain in news_domains.items():
        print(f"\n{name} Headlines:")
        print(domain.extract_headlines())


if __name__ == "__main__":
    main()
