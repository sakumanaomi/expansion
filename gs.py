"""
G's ACADEMY からサンプル取得
"""
import os
from urllib.request import urlopen
from pprint import pprint
from bs4 import BeautifulSoup

with urlopen("http://gsacademy.jp/mentor-lecturer") as res:
    html = res.read().decode("utf-8")

soup = BeautifulSoup(html,"html.parser")

# img_urls = [e["src"] for e in soup.select(".heading.c2 img")]
img_urls = [e["src"] for e in soup.select(".mentor__list-item-img img")]

# img_urls = [u if u.find("http") == 0 else "http://gsacademy.tokyo" + u for u in img_urls]
img_urls = [u if u.find("http") == 0 else "http://gsacademy.jp" + u for u in img_urls]

if not os.path.exists("img"):
    os.mkdir("img")

for i, url in enumerate(img_urls):
    print(i, url)
    with urlopen(url) as res:
        img = res.read()
        with open("img/%d.png" % (i+1),"wb") as f:
            f.write(img)