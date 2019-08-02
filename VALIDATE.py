from tqdm import tqdm
from time import sleep
import requests
import math
import argparse

parser = argparse.ArgumentParser(
    description="Office 365 'Xerox' Campaign Validation Script @littl3field"
)

parser.add_argument('QUERY', help="Query a user or domain")
args = parser.parse_args()

def textRequest():
    result = []
    with open('urls.txt', 'r') as r:
        urls = r.read()
        urls = filter(None, urls.split("\n"))
        for url in urls:
            req = requests.get(url)
            if req.status_code != 200:
                print('[Error] URL is dead:')
                continue
            result.append(req.content.decode())

    with open('result.txt', 'a') as w:
        for load in tqdm(range(0, 100), desc="[INFO] Pulling Data:", ascii=True):
            sleep(.01)
            for res in result:
                w.write(res)

#Check if string is contained in userlist
def check(query_arg):
    with open('result.txt', 'r') as searchfile:
        for load in tqdm(range(0, 100), desc="[INFO] Querying Data:", ascii=True):
            sleep(.01)
            o = open('matches.txt', 'a')
            for line in searchfile:
                if query_arg.lower() in line.lower():
                    output_str = "Targeted User Found: " + line
                    o.write("Targeted  User Found: " + line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Office 365 'Xerox' Campaign Validation Script"
    )

    parser.add_argument('QUERY', help="Query a user or domain")
    args = parser.parse_args()
    textRequest()
    check(args.QUERY)
