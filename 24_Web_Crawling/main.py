from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/scrape")
def get_news():
    url = "https://indianexpress.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = []

    for item in soup.find_all("a", class_="article-click topblockNews__sidebarLink"):
        title.append(item.text)

    return {
        "title": title,
    }