import requests
from datetime import datetime
import os

day = datetime.today().replace(microsecond=0)

title = str(datetime.today().year) + '-' + str(datetime.today().month) + '-' + str(datetime.today().day) + '.txt'
print(day)
print(title)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE_DIR + "/logs", title), "a+") as f:
    f.write("End Market2.py " + str(datetime.now()) + " " + '1' + "\n")
"""
with open(os.path.join(BASE_DIR, "log.txt"), "a+") as f:
    f.write("End Market2.py " + str(datetime.now()) + " " + articles + "\n")
"""