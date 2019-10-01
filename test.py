import requests
from datetime import datetime
import os
import DataCheck

test = [
    "17092777", "16917320", "16993839", # 냉장고
    "17093452", "17093425", # 아이폰
    "17093483", "17093424", # 갤럭시
    "17092990", "17016755", # LG
    "16526482", "16295337", "15791538", "17085434", # TV
]

for articles in test:
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
    try:
        DataCheck.DataCheck(title, price, URL, day, description)
    except Exception:
        with open(os.path.join(BASE_DIR, "Error.txt"), "a+") as f:
            f.write("Error URL : " + URL)

    articles = str(int(articles) + 2)
    count = 0

request.close()