import requests
from datetime import datetime
import os
import DataCheck
import crawlbotlogging


start = 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE_DIR, "startBungae1.txt"), "r") as f:
    start = int(f.readline())

articles = str(start)
count = 0

end = 0

startTime = datetime.now()
crawlbotlogging.startLog("Bungae1.py", articles)

while 1:
    URL = 'https://core-api.bunjang.co.kr/api/1/product/'
    URL2 = '/detail_info.json?stat_uid=9056251&version=2'
    URL = URL + articles + URL2
    # print(URL)
    request = requests.get(URL)
    html = request.json()

    if html["result"] == "fail":
        count += 1
        articles = str(int(articles) + 2)
        if count >= 10:
            articles = str(int(articles) - 20)
            break
        continue

    if html['item_info'] == None:
        # print('None')
        count += 1
        articles = str(int(articles) + 2)
        if count >= 10:
            articles = str(int(articles) - 20)
            break
        continue

    elif html['item_info']['status'] == "3":
        # print('Trade')
        count += 1
        articles = str(int(articles) + 2)
        if count >= 10:
            articles = str(int(articles) - 20)
            break
        continue
    else:
        title = html['item_info']['name']
        price = html['item_info']['price']
        description = html['item_info']['description']
        day = datetime.today().replace(microsecond=0)

    URL = 'https://m.bunjang.co.kr/products/' + articles
    if int(price) < 10000:
        articles = str(int(articles) + 2)
        continue

    # print(title, price, day, URL, description)
    try:
        DataCheck.DataCheck(title, str(price), URL, day, description, 2)
    except Exception:
        with open(os.path.join(BASE_DIR, "Error.txt"), "a+") as f:
            f.write("Error URL : " + URL + "\n")

    articles = str(int(articles) + 2)
    count = 0

request.close()

with open(os.path.join(BASE_DIR, "startBungae1.txt"), "w") as f:
    f.write(articles)

crawlbotlogging.endLog("Bungae1.py", articles, startTime)
