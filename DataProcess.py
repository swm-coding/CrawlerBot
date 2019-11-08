import re
import math
from pymongo import MongoClient

def _getCompany(text):
    companyList = [
        ['삼성', 'SAMSUNG', '갤럭시', '삼성전자'],
        ['LG', '엘지', '엘쥐', 'LG전자'],
        ['ASUS', '에이수스'],
        ['APPLE', '맥북', '애플', '아이맥', '에어팟', '아이패드', '아이팟'],
        ['CANON', '캐논'],
        ['신도리코'],
        ['EPSON'],
        ['샤오미'],
        ['한성컴퓨터', '한성'],
        ['BENQ', '벤큐'],
        ['CORSAIR', '커세어'],
        ['DECK', '덱'],
        ['알파스캔'],
        ['HP'],
        ['LENOVO', '레노버', '레노보'],
        ['롯데하이마트', '롯데', '하이마트'],
        ['소니', 'SONY'],
        ['제닉스'],
        ['QCY'],
        ['JBL'],
        ['ABKO', '앱코'],
        ['MSI'],
        ['BRITZ'],
        ['웨이코스'],
        ['맥스틸'],
        ['로지텍', 'LOGITECH'],
        ['MAXTILL'],
        ['RAZER'],
        ['위니아딤채', '딤채'],
        ['쿠쿠전자', '쿠쿠'],
        ['쿠첸'],
        ['알파스캔'],
    ]

    for companyNames in companyList:
        for companyName in companyNames:
            if companyName in text:
                return companyNames[0]

    return ''


def _getCpu(text):
    if "I3" in text:
        return 'Intel i3'

    if "I5" in text:
        return 'Intel i5'

    if "I7" in text:
        return 'Intel i7'

    if "라이젠3" or "라이젠 3" in text:
        return "Ryzen 3"

    if "라이젠5" or "라이젠 5" in text:
        return "Ryzen 5"

    if "라이젠7" or "라이젠 7" in text:
        return "Ryzen 7"


def _getGpu(text):
    if not "GTX" or "GT" in text:
        return ''

    GPU = [
        "705", "710", "720", "730", "740", "745", "750", "750TI", "760", "770", "780", "780TI",
        "950", "960", "970", "980", "980TI",
        "1050", "1060", "1070", "1080", "1080TI",
        "1650", "1660", "1660TI",
        "2060", "2070", "2080", "2080TI",
        "GTX TITAN X", "TITAN V", "TITAN RTX"
    ]

    for i in GPU:
        if i in text:
            return i
    return ''


def _getRam(text):
    text = "\n" + text + "\n"
    ramDeclares = ['램', 'RAM']
    candidate = []

    for Declare in ramDeclares:
        idx = text.find(Declare)

        if text[idx - 1] == "그":
            idx = text.find(Declare, idx + 1)

        if idx == -1:
            continue

        # leave only one line that includes declare
        line = text[text.rfind("\n", 0, idx) + 1:text.find("\n", idx)]
        idx = line.find(Declare)

        post = re.search(r'\d+', line[idx:])
        if post != None:
            candidate.append(int(post.group()))
        pre = re.search(r'\d+', line[idx::-1])
        if pre != None:
            candidate.append(int(pre.group()[::-1]))

    if len(candidate) == 0:
        return -1

    def ramSort(val):
        if val <= 0:
            return -1
        return -bin(val).count("1") * 10000 - abs(math.log2(val) - 2.5) * 100 + val

    return sorted(candidate, key=ramSort, reverse=True)[0]


def _getSsd(text):
    # TODO: discuss whether to seperate ssd hdd
    text = "\n" + text + "\n"
    ssdDeclares = ['스스디', 'SSD']
    candidate = []

    for Declare in ssdDeclares:
        idx = text.find(Declare)

        if idx == -1:
            continue

        # leave only one line that includes declare
        line = text[text.rfind("\n", 0, idx) + 1:text.find("\n", idx)]
        idx = line.find(Declare)

        post = re.search(r'\d+', line[idx:])
        if post != None:
            candidate.append(int(post.group()))
        pre = re.search(r'\d+', line[idx::-1])
        if pre != None:
            candidate.append(int(pre.group()[::-1]))

    if len(candidate) == 0:
        return -1

    def ssdSort(val):
        if val <= 0:
            return -1
        return -bin(val).count("1") * 10 - abs(math.log2(val) - 7.5)

    return sorted(candidate, key=ssdSort, reverse=True)[0]

def _getHdd(text):
    # TODO: discuss whether to seperate ssd hdd
    text = "\n" + text + "\n"
    ssdDeclares = ['HDD', '하드', '하드디스크']
    candidate = []

    for Declare in ssdDeclares:
        idx = text.find(Declare)

        if idx == -1:
            continue

        # leave only one line that includes declare
        line = text[text.rfind("\n", 0, idx) + 1:text.find("\n", idx)]
        idx = line.find(Declare)

        post = re.search(r'\d+', line[idx:])
        if post != None:
            candidate.append(int(post.group()))
        pre = re.search(r'\d+', line[idx::-1])
        if pre != None:
            candidate.append(int(pre.group()[::-1]))

    if len(candidate) == 0:
        return -1

    def ssdSort(val):
        if val <= 0:
            return -1
        return -bin(val).count("1") * 10 - abs(math.log2(val) - 9.5)

    return sorted(candidate, key=ssdSort, reverse=True)[0]


def _getDisplay(text):
    def _get_first_nbr_from_str(input_str):
        '''
        :param input_str: strings that contains digit and words
        :return: the number extracted from the input_str
        demo:
        'ab324.23.123xyz': 324.23
        '.5abc44': 0.5
        '''
        try:
            if not input_str and not isinstance(input_str, str):
                return 0
            out_number = ''
            for ele in input_str:
                if (ele == '.' and '.' not in out_number) or ele.isdigit():
                    out_number += ele
                elif out_number:
                    break
            return float(out_number)
        except ValueError:
            return -1.0

    def _get_last_nbr_from_str(input_str):
        '''
        :param input_str: strings that contains digit and words
        :return: the number extracted from the input_str
        demo:
        'ab324.23.123xyz': 23.123
        '.5abc44': 44
        '''
        input_str = input_str[::-1]
        try:
            if not input_str and not isinstance(input_str, str):
                return 0
            out_number = ''
            for ele in input_str:
                if (ele == '.' and '.' not in out_number) or ele.isdigit():
                    out_number += ele
                elif out_number:
                    break
            # print(out_number,out_number[::-1])
            return float(out_number[::-1])
        except ValueError:
            return -1.0

    text = "\n" + text + "\n"
    displayDeclares = ['인치', '"', "''"]
    candidate = []

    for Declare in displayDeclares:
        idx = text.find(Declare)

        if idx == -1:
            continue

        # leave only one line that includes declare
        line = text[text.rfind("\n", 0, idx) + 1:text.find("\n", idx)]
        idx = line.find(Declare)

        post = _get_first_nbr_from_str(line[idx:])
        if post != -1:
            candidate.append(post)
        pre = _get_last_nbr_from_str(line[:idx])
        if pre != -1:
            candidate.append(pre)

    if len(candidate) == 0:
        return -1.0

    def displaySort(val):
        return -abs(val - 14)

    return sorted(candidate, key=displaySort, reverse=True)[0]

def _getDisplayTech(text):
    List = ["OLED", "QLED", "UHD", "FHD", "HD"]

    for i in List:
        if i in text:
            return i

def _getRefgrigeratorSize(text):
    # TODO: 냉장고 용량 데이터 처리 '리터' 'L' 구분,
    return ''

def _getWasherSize(text):
    # TODO: 냉장고 용량 데이터 처리 '리터' 'L' 구분,
    return ''

def _getf2f(text):
    if "직거래" in text:
        return 1

    return 0

def SmartPhone(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.smartphone
    coll.insert(data)

def Tablet(title, price, URL, time, text, site):
    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.tablet
    coll.insert(data)

def SmartWatch(title, price, URL, time, text, site):
    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.smartwatch
    coll.insert(data)


def DigitalCamera(title, price, URL, time, text, site):
    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.digitalcamera
    coll.insert(data)

def DSLR(title, price, URL, time, text, site):
    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.dslr
    coll.insert(data)

def ActionCamera(title, price, URL, time, text, site):
    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.actioncamera
    coll.insert(data)


def KimchiRefrigerator(title, price, URL, time, text, site):

    company = _getCompany(title)
    size = _getRefgrigeratorSize(text)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "size": size,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.kimchirefrigerator
    coll.insert(data)

def Refrigerator(title, price, URL, time, text, site):

    company = _getCompany(title)
    size = _getRefgrigeratorSize(text)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "size": size,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.refrigerator
    coll.insert(data)

def ElectronicRice(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.electronicrice
    coll.insert(data)

def Induction(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.induction
    coll.insert(data)

def Electronic(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.electronic
    coll.insert(data)

def Oven(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.oven
    coll.insert(data)

def ElectronicPort(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.electronicport
    coll.insert(data)

def Mixer(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.mixer
    coll.insert(data)

def CofeeMachine(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.coffeemachine
    coll.insert(data)

def DishesWashing(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.disheswashing
    coll.insert(data)

def DishesDrying(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.dishesdrying
    coll.insert(data)

def FoodTrash(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.foodtrash
    coll.insert(data)


def Washer(title, price, URL, time, text, site):

    company = _getCompany(title)
    size = _getWasherSize(text)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "size": size,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.washer
    coll.insert(data)

def ElectronicCleaning(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.electroniccleaning
    coll.insert(data)


def TV(title, price, URL, time, text, site):

    company = _getCompany(title)
    display = _getDisplay(text)
    displayTech = _getDisplayTech(text)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "display": display,
        "displayTech" : displayTech,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.tv
    coll.insert(data)

def AirCondition(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.aircondition
    coll.insert(data)

def Heater(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.heater
    coll.insert(data)

def AirWasher(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.airwasher
    coll.insert(data)

def Humidification(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.humidification
    coll.insert(data)

def Dehumidification(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.dehumidification
    coll.insert(data)

def WaterPurifer(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.waterpurifer
    coll.insert(data)


def GameMachine(title, price, URL, time, text, site):
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.gamemachine
    coll.insert(data)

def DestkTop(title, price, URL, time, text, site):

    f2f = _getf2f(text)
    cpu = _getCpu(text)
    gpu = _getGpu(text)
    ram = _getRam(text)
    ssd = _getSsd(text)
    hdd = _getHdd(text)

    data = {
        "title": title,
        "price": price,
        "cpu": cpu,
        "gpu": gpu,
        "ram": ram,
        "ssd": ssd,
        "hdd": hdd,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.desktop
    coll.insert(data)

def Monitor(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.monitor
    coll.insert(data)

def Keyboard(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.keyboard
    coll.insert(data)

def Mouse(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.mouse
    coll.insert(data)

def efm(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.efm
    coll.insert(data)


def Laptop(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)
    cpu = _getCpu(text)
    ram = _getRam(text)
    ssd = _getSsd(text)
    display = _getDisplay(text)

    data = {
        "title" : title,
        "price" : price,
        "company" : company,
        "cpu" : cpu,
        "ram" : ram,
        "ssd" : ssd,
        "display" : display,
        "time" : time,
        "url" : URL,
        "text" : text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.laptop
    coll.insert(data)

def PrinterScanner(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.printerscanner
    coll.insert(data)

def Printer(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.printer
    coll.insert(data)

def Scanner(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.scanner
    coll.insert(data)


def Speaker(title, price, URL, time, text, site):

    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site" : site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.speaker
    coll.insert(data)

def HeadPhone(title, price, URL, time, text, site):
    company = _getCompany(title)
    f2f = _getf2f(text)

    data = {
        "title": title,
        "price": price,
        "company": company,
        "time": time,
        "url": URL,
        "text": text,
        "f2f": f2f,
        "site": site
    }

    client = MongoClient("mongodb://dev:dev@13.125.4.46:27017/test")
    coll = client.test.headphone
    coll.insert(data)


