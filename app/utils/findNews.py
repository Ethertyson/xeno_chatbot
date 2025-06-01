# Created by Priatnshu on 2025-05-31

from app.extensions import get_google_news_client

def fetchLatestNews():
    response = get_google_news_client()
    newsData = response.json()

    latestNews = ''
    for idx, article in enumerate(newsData.get('articles', [])):
        title = article.get('title', 'No title')
        description = article.get('description', 'No description available')
        url = article.get('url', 'No URL')
        source = article.get('source', {}).get('name', 'Unknown source')

        latestNews += (
            f"{source.upper()}\n"
            f"{title}\n"
            f"{description}\n"
            f"ReadMore at: {url}"
        )

    return latestNews