import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("span", class_="titleline")

with open("news_links.txt", "w", encoding="utf-8") as file:
    for article in articles:
        link_tag = article.find("a")
        
        if link_tag:
            title = link_tag.text
            link = link_tag["href"]
            file.write(f"{title}\n{link}\n{''}\n")
