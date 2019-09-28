from bs4 import BeautifulSoup
from datetime import datetime
import process
from pymongo import MongoClient
import tester
import requests
import os

start = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "startMarket2.txt"), "r") as f:
    start = int(f.readline())

articles = str(start)
count = 0

end = 0

with open(os.path.join(BASE_DIR, "log.txt"), "a+") as f:
    f.write("Start Market2.py " + str(datetime.now()) + " " + articles + "\n")

while 1:
    URL = 'https://www.daangn.com/articles/'
    URL = URL + articles
    print(URL)

    request = requests.get(URL)
    html = request.text
    soup = BeautifulSoup(html, 'html.parser')

    Check = soup.find('div', class_="error-image")
    if Check:
        count += 1
        articles = str(int(articles) + 2)
        if count >= 10:
            articles = str(int(articles) - 20)
            break
        continue

    repoCheck = soup.find('p', id='no-article')
    if repoCheck:
        count += 1
        articles = str(int(articles) + 2)
        if count >= 10:
            articles = str(int(articles) - 20)
            break
        continue

    try:
        title = soup.find('h1', id='article-title').contents[0]
    except Exception:
        articles = str(int(articles) + 2)
        continue

    id = soup.find('div', id='nickname').contents[0]

    try:
        price = soup.find('p', id='article-price').contents[0]
    except Exception:
        price = '0원'

    if len(price) < 6:
        price = '0원'

    else:
        price = soup.find('p', id='article-price').contents[0]
        price = price.replace(" ", '').replace("\n", "")

    day = datetime.today().replace(microsecond=0)

    try:
        description = soup.find('div', id='article-detail')
    except Exception:
        articles = str(int(articles) + 2)
        continue

    description = description.text

    print(title, price, day, URL, description)

    articles = str(int(articles) + 2)
    count = 0

    """
    데이터 분석 및 몽고디비 연결
    """
    """
    수정해야함
    post = {
        "title": title,
        "price": price,
        "url": URL,
        "time": day,
        "text": description,
        "id": id
    }

    result = process.process(post)

    if tester.isLaptopPost(title) and result["count"] > 0:
        client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
        coll = client.test.laptop
        coll.insert(result["data"])
        print("Laptop Post Found!")
    """

request.close()

with open(os.path.join(BASE_DIR, "startMarket2.txt"), "w") as f:
    f.write(articles)

with open(os.path.join(BASE_DIR, "log.txt"), "a+") as f:
    f.write("End Market2.py " + str(datetime.now()) + " " + articles + "\n")
