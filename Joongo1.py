import requests
from datetime import datetime
import os

start = 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "startJoongo1.txt"), "r") as f:
    start = int(f.readline())

articles = str(start)
count = 0

end = 0

with open(os.path.join(BASE_DIR, "log.txt"), "a+") as f:
    f.write("Joongo1.py " + str(datetime.now()) + " " + articles + "\n")

while 1:
    URL = 'https://api.joongna.com/product/'
    URL = URL + articles
    print(URL)
    try:
        request = requests.get(URL)
    except Exception:
        articles = str(int(articles) + 2)

    if request.status_code == 400:
        count += 1
        articles = str(int(articles) + 2)
        if count >= 10:
            articles = str(int(articles) - 20)
            break
        continue

    html = request.json()
    title = html['data']['productTitle']
    price = html['data']['productPrice']
    description = html['data']['productDescription']
    day = datetime.today().replace(microsecond=0)

    URL = 'https://m.joongna.com/product-detail/' + articles
    if price < 10000:
        articles = str(int(articles) + 2)
        continue

    print(title, price, day, URL, description)
    """
    데이터 분석 및 몽고디비 연결
    """

    articles = str(int(articles) + 2)
    count = 0

request.close()

with open(os.path.join(BASE_DIR, "startJoongo1.txt"), "w") as f:
    f.write(articles)
