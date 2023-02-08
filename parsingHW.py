import csv
import re
import requests
from bs4 import BeautifulSoup


def write_csv(data):
    with open("menu.csv", "a") as file:
        writer = csv.writer(file, lineterminator='\r', delimiter=";")
        writer.writerow((data['name'],
                         data['grams'],
                         data['price'],
                         data['composition']))


def refined(s):
    res = re.sub(r"[a-я,₽,\\]", "", s)
    return res


def get_html(url):
    rq = requests.get(url)
    return rq.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all("div", class_='mainCard_cardInfoWrapper__v_WW4 mainCard_catalog___UIKE')
    for element in elements:
        try:
            name = element.find("h1").text
        except ValueError:
            name = ""
        try:
            grams = element.find("span", class_='mainCard_weight__2L9G0').text
        except ValueError:
            grams = ""
        try:
            price = refined(element.find("div", class_='mainCard_price__bRnuU').text) + " rub"
        except ValueError:
            price = ""
        try:
            comp = element.find("div", class_='mainCard_text-container__MimBT mainCard_productSelectedText__zjaSo')
            final_comp = comp.find_all("div")[-1].text
        except ValueError:
            final_comp = ""
        data = {"name": name,
                "grams": grams,
                "price": price,
                "composition": final_comp}
        write_csv(data)


def main():
    url = "https://ilovesakura.ru/spb/menu/rolly"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
