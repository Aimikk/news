import requests
from bs4 import BeautifulSoup


def fetch_google_news():
    url = 'https://news.google.com/rss'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    headlines = []
    for item in soup.find_all('item')[:500]:  # Limit to 500 headlines
        title = item.title.text
        link = item.link.text
        headlines.append({'title': title, 'link': link})

    return headlines


news = fetch_google_news()
for i, article in enumerate(news, 1):
    print(f"{i}. {article['title']}\n   {article['link']}\n")
