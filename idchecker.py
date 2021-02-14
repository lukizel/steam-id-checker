import requests
from bs4 import BeautifulSoup

with open('input.txt') as f:
    id = [line.rstrip() for line in f]
print(id)
available = []

for x in id:
    resp = requests.get("http://steamcommunity.com/id/{}".format(x))
    bsoup = BeautifulSoup(resp.text, 'html.parser')
    counter = id.index(x)
    amount = len(id)
    hasname = bsoup.find("div", {"class": "persona_name"})
    if hasname:
        print("[",counter,"/",amount,"]", " [Taken] " , x, sep='')
    else:
            print("[", counter, "/", amount, "]", " [Available] ", x, sep='')
            available.append(x)

with open('output_available.txt', 'w') as f:
    for item in available:
        f.write("%s\n" % item)