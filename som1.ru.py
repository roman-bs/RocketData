import requests
from bs4 import BeautifulSoup
import json


# url = "https://som1.ru/shops/"
#
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.934 (beta) Yowser/2.5 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
#
#
# with open("index1.html", 'w') as file:
#     file.write(src)


with open("index1.html") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")
all_shop_hrefs = soup.find_all(class_="shops-col shops-button")


for item in all_shop_hrefs:
    item_href = item.get('href')
    print(f'{item_href}')