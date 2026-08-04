from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/scrape")
def get_news(page: int = 1, limit: int = 10):
    url = "https://indianexpress.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = []

    for item in soup.find_all("a", class_="article-click topblockNews__sidebarLink"):
        title.append(item.text)

    # pagination logic
    start = (page - 1) * limit
    end = start + limit
    return {
        "page": page,
        "limit": limit,
        "total_titles": len(title),
        "titles": title[start:end]
    }