import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

sites = [
    "https://montsame.mn",
]

news_list = []

for site in sites:

    html = requests.get(site).text
    soup = BeautifulSoup(html,"html.parser")

    links = soup.select("a")

    for link in links:

        title = link.text.strip()

        if len(title) > 30:

            news_list.append({
                "title": title,
                "url": link.get("href"),
                "time": str(datetime.now())
            })

with open("news.json","w",encoding="utf8") as f:

    json.dump(news_list,f,ensure_ascii=False,indent=2)
