from bs4 import BeautifulSoup
import requests
import urllib
from pprint import pprint
import re

res = requests.get("https://zh.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E5%88%97%E8%A1%A8")
soup = BeautifulSoup(res.content.decode("utf-8"), "html.parser")
tags = soup.select("#mw-content-text > div > ul > li")
st = ""
for tag in tags:
    try:
        no, name = tag.text.split(" ",1)
    except:
        try:
            g = re.match("(\d+)(\S+)", tag.text)
            no, name = g.groups()
        except:
            pass
    st += "{},{}\n".format(no.strip(), name.strip())
with open("code.csv", "w", encoding="utf-8") as f:
    f.write(st)
