#!/usr/bin/python
from tqdm import tqdm
from time import sleep
import requests

#Enter query here (this is case sensitive)
QUERY = "company"

def textRequest():
    result = []
    with open('urls.txt', 'r') as r:
        urls = r.read()
        for url in urls.split('\n'):
            req = requests.get(url)
            if req.status_code != 200:
                print('[Error] URL is dead:' + url)
            else:
                continue
            result.append(req.content.decode())

    with open('result.txt', 'a') as w:
        for load in tqdm(range(0, 100), desc="[INFO] Pulling Data:", ascii=True):
            sleep(.01)
            for res in result:
                w.write(res)

#Check if string is contained in userlist
def check():
        with open('result.txt', 'r') as searchfile:
            for load in tqdm(range(0, 100), desc="[INFO] Querying Data:", ascii=True):
                sleep(.01)
                for line in searchfile:
                    if QUERY in line:
                        o = open('matches.txt', 'w')
                        print("Targeted User Found: " + line, file=o)

if __name__ == '__main__':
    textRequest()
    check()
