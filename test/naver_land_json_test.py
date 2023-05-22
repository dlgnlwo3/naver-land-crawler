import requests
from bs4 import BeautifulSoup
import json

keyword = "경기도 구리시"

url = f"https://m.land.naver.com/search/result/{keyword}"

print(url)

print()

res = requests.get(url)
res.raise_for_status()


soup = (str)(BeautifulSoup(res.text, "lxml"))

print(soup)

print()
