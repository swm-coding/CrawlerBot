# 번개장터
# https://m.bunjang.co.kr/
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import os

start = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "startBungae3.txt"), "r") as f:
    start = int(f.readline())

options = webdriver.ChromeOptions()
options.add_argument('--dislable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

articles = str(start)
count = 0
end = 0

with open(os.path.join(BASE_DIR, "log.txt"), "a+") as f:
    f.write("Bungae3.py " + str(datetime.now()) + " " + articles + "\n")

path=BASE_DIR + "/chromedriver_linux"
print(path)

driver = webdriver.Chrome(options=options, executable_path=path)

while 1:
    URL = 'https://m.bunjang.co.kr/products/'
    URL = URL + articles

    print(URL)

    try:
        driver.get(URL)
    except Exception:
        articles = str(int(articles) + 4)
        count += 1
        if count >= 10:
            articles = str(int(articles) - 40)
            break
        continue

    try:
        html = driver.page_source
    except Exception:
        articles = str(int(articles) + 4)
        count += 1
        if count >= 10:
            articles = str(int(articles) - 40)
            break
        continue

    soup = BeautifulSoup(html, 'html.parser')

    repoCheck = soup.find('div', class_='suggested-products-title')
    if repoCheck:
        count += 1
        articles = str(int(articles) + 4)
        if count >= 10:
            articles = str(int(articles) - 40)
            break
        continue

    try :
        title = (soup.find('div', class_='product-summary__title').find('h2')).contents[0]
    except Exception:
        articles = str(int(articles) + 4)
        continue

    try:
        description = soup.find('p', class_='description').contents[0]
    except Exception:
        articles = str(int(articles) + 4)
        continue

    price = (soup.find('div', class_='product-summary__title').find('h3')).contents[0]
    if len(price) <= 5:
        articles = str(int(articles) + 4)
        continue

    day = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)
    price += '원'

    print(title, price, day, URL, description)

    """
    데이터 분석 및 몽고디비 연결
    """

    articles = str(int(articles) + 4)
    count = 0

os.remove(os.path.join(BASE_DIR,  "startBungae3.txt"))

with open(os.path.join(BASE_DIR, "startBungae3.txt"), "w") as f:
    f.write(articles)
