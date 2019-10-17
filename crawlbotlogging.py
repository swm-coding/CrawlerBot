from datetime import datetime
import os

def startLog(crawlerbotName, articles):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_title = str(datetime.today().year) + '-' + str(datetime.today().month) + '-' + str(datetime.today().day) + '.txt'
    with open(os.path.join(BASE_DIR + "/logs", log_title), "a+") as f:
        f.write(str(datetime.now()) + ": Starting " + crawlerbotName + " with " + articles + "\n")

def endLog(crawlerbotName, articles, starttime):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    log_title = str(datetime.today().year) + '-' + str(datetime.today().month) + '-' + str(datetime.today().day) + '.txt'
    with open(os.path.join(BASE_DIR + "/logs", log_title), "a+") as f:
        f.write(str(datetime.now()) + ": Ending   " + crawlerbotName + " with " + articles + " in " + str(int(((datetime.now()-starttime).total_seconds()))) + " seconds\n")