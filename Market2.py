from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os
import DataCheck
import crawlbotlogging


start = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

log_title = str(datetime.today().year) + '-' + str(datetime.today().month) + '-' + str(datetime.today().day) + '.txt'

with open(os.path.join(BASE_DIR, "startMarket2.txt"), "r") as f:
    start = int(f.readline())

articles = str(start)
count = 0

end = 0

startTime = datetime.now()
crawlbotlogging.startLog("Market2.py", articles)

while 1:
    URL = 'https://www.daangn.com/articles/'
    URL = URL + articles
    # print(URL)

    try:
        request = requests.get(URL)
    except Exception:
        articles = str(int(articles) + 2)

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
        articles = str(int(articles) + 2)
        continue

    if len(price) <= 6:
        articles = str(int(articles) + 2)
        continue

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
    price = price.replace(',', '')
    price = price[:-1]

    if len(price) <= 4:
        articles = str(int(articles) + 2)
        continue

    # print(title, price, day, URL, description)
    try:
        DataCheck.DataCheck(title, str(price), URL, day, description, 3)
    except Exception:
        with open(os.path.join(BASE_DIR, "Error.txt"), "a+") as f:
            f.write("Error URL : " + URL + "\n")

    articles = str(int(articles) + 2)
    count = 0

request.close()

with open(os.path.join(BASE_DIR, "startMarket2.txt"), "w") as f:
    f.write(articles)

crawlbotlogging.endLog("Market2.py", articles, startTime)
