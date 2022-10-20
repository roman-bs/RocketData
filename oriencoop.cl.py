import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import json
import re

# url = "https://oriencoop.cl/sucursales.htm"
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
# with open("index.html", 'w') as file:
#     file.write(src)


with open("index.html") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")
data = soup.find(class_="s-dato").find_all('span') # парсинг выбранного тега
data_name = soup.find(class_="s-dato").find('h3')



m = re.search(r'2d=(\d+\.\d+),(\d+\.\d+)', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d6689.174124950521!2d-71.625896!3d-33.041008!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9689e12eaa95f955%3A0xcf70834bd8c5ef8c!2sEsmeralda+940%2C+Valpara%C3%ADso%2C+Regi%C3%B3n+de+Valpara%C3%ADso%2C+Chile!5e0!3m2!1ses!2sus!4v1495663213494')
print(m.groups())

z =

address = "address"
name = "name"
phones = "phones"
working_hours = "working_hours"
all_data_dict = {}


all_data_dict[address] = data[0].text
all_data_dict[name] = data_name.text
all_data_dict[phones] = data[1].text
all_data_dict[working_hours] = data[3].text, data[4].text


with open("all_data.json", "w") as file:
    json.dump(all_data_dict, file, indent=4, ensure_ascii=False)




