# 중고나라 모바일 버전
# https://m.joongna.com

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import os
import requests

start = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "startJoongo2.txt"), "r") as f:
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
    f.write("Joongo2.py " + str(datetime.now()) + " " + articles + "\n")

path=BASE_DIR + "/chromedriver"
print(path)

driver = webdriver.Chrome(options=options, executable_path=path)

while 1:

    URL = 'https://m.joongna.com/product-detail/'
    URL = URL + articles
    try:
        driver.get(URL)
    except Exception:
        articles = str(int(articles) + 4)
        count += 1
        if count >= 10:
            articles = str(int(articles) - 40)
            break
        continue

    print(URL)

    request = requests.get(URL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    data = soup.find('section', id='pdtMainData')

    if not data.find('div', class_='data').find('p').contents:
        count += 1
        articles = str(int(articles) + 4)
        if count >= 10:
            articles = str(int(articles) - 40)
            break
        print('Not Products')
        continue

    else:
        title = data.find('div', class_='data').find('p').contents[0]
        price = data.find('div', class_='data').find('em').contents[0]
        day = str(datetime.now().year) + '-' + str(datetime.now().month) + '-' + str(datetime.now().day)

        try:
            description = data.find('article', class_='detail_atc bg_white').find('p', class_='description mt20').find('span').contents[0]
        except Exception:
            description = ""

    print(title, price, day, URL, description)

    """
    데이터 분석 및 몽고디비 연결
    """

    articles = str(int(articles) + 4)
    count = 0

driver.close()


os.remove(os.path.join(BASE_DIR,  "startJoongo2.txt"))

with open(os.path.join(BASE_DIR, "startJoongo2.txt"), "w") as f:
    f.write(articles)
