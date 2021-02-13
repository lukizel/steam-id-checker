import requests
from bs4 import BeautifulSoup

with open('input.txt') as f:
    id = [line.rstrip() for line in f]
print(id)
available = []

for x in id:
    resp = requests.get("http://steamcommunity.com/id/{}".format(x))
    bsoup = BeautifulSoup(resp.text, 'html.parser')
    hasname = bsoup.find("div", {"class": "persona_name"})
    if hasname:
        print("[Taken]    ", x)
    else:
            print("[Available]", x)
            available.append(x)

with open('output_available.txt', 'w') as f:
    for item in available:
        f.write("%s\n" % item)




