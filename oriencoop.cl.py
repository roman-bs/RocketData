import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import json


url = "https://oriencoop.cl/sucursales.htm"


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.934 (beta) Yowser/2.5 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text


with open("index.html", 'w') as file:
    file.write(src)


with open("index.html") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")
data = soup.find(class_="s-dato").find_all('span') # парсинг выбранного тега
data_name = soup.find(class_="s-dato").find('h3')


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




