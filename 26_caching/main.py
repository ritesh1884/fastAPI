from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time   # it will tell ki caching ke pehle kitna time laga tha aur caching ke baad kitna time laga

app = FastAPI()

# storing the chache
cache_dat = []
last_fetch = 0

@app.get("/scrape")
def get_news():
    global cache_dat, last_fetch

    start_time = time.time()
    if time.thread_time() - last_fetch > 60:  # if the last fetch was less than 60 seconds ago, return the cached data
        print("Fetching new data...")
        url = "https://news.ycombinator .com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        cache_data = [
            item.text for item in soup.find_all("a", class_="storylink")
        ]

        last_fetch = time.time()

    else: 
        print("Using cache data")

    end = time.time()
    time_taken = round(end - start_time, 4)
    print("Time taken:", time_taken)

    return {
        "time_taken": time_taken,
        "titles": cache_data
    }

   