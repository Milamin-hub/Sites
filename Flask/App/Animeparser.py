import os
import requests
from bs4 import BeautifulSoup



latest_anime = "https://animevost.org/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
full_page = requests.get(latest_anime, headers)

soup = BeautifulSoup(full_page.content, "html.parser")

convert = soup.findAll("h2")
list_i = []

for i in range(len(convert)):
    c_i = convert[i].text.strip()
    list_i.append(c_i)


