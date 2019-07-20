# 당근마켓
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os

start = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "startMarket2.txt"), "r") as f:
    start = int(f.readline())
with open(os.path.join(BASE_DIR, "log.txt"), "a+") as f:
    f.write(str(datetime.now()) +" Daangn2\n")
articles = str(start)
count = 0

end = 0

while 1:
    URL = 'https://www.daangn.com/articles/'
    URL = URL + articles

    request = requests.get(URL)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')

    Check = soup.find('div', class_="error-image")
    if Check:
        count += 1
        articles = str(int(articles) + 2)
        if count >= 5:
            articles = str(int(articles) - 10)
            break
        continue

    repoCheck = soup.find('p', id='no-article')
    if repoCheck :
        count += 1
        articles = str(int(articles) + 2)
        if count >= 5:
            articles = str(int(articles) - 10)
            break
        continue

    count = 0

    try:
        title = soup.find('h1', id='article-title').contents[0]
    except Exception:
        articles = str(int(articles) + 2)
        continue

    price = soup.find('p', id='article-price-nanum')
    if price :
        price = '무료나눔'
        articles = str(int(articles) + 2)
        continue
    else:
        price = soup.find('p', id='article-price').contents[0]
        if len(price) <= 6:
            articles = str(int(articles) + 2)
            continue

    try:
        description = soup.find('div', id='article-detail')
    except Exception:
        articles = str(int(articles) + 2)
        continue

    price = price.strip()
    day = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)

    articles = str(int(articles) + 2)
    print(title, price, day, URL, 1)

request.close()

os.remove(os.path.join(BASE_DIR, "startMarket2.txt"))

with open(os.path.join(BASE_DIR, "startMarket.txt"), "w") as f:
    f.write(articles)
