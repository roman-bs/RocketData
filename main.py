import requests


def get_data():
    url = "https://oriencoop.cl/sucursales.htm"
    r = requests.get(url=url)

    with open("index11.html", "w") as file:
        file.write(r.text)



def main():
    get_data()


if __name__ == '__main__':
    main()