import requests
from bs4 import BeautifulSoup

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.title.string