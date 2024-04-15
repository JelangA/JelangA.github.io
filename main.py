import json

from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


def scraping():
    page = requests.get("https://www.republika.co.id/")
    obj = BeautifulSoup(page.text, 'html.parser')

    news_list = []

    for headline in obj.find_all('li', class_='list-group-item list-border conten1'):
        tanggal = headline.find('div', class_='date').text.strip()
        judul = headline.h3.text.strip()
        news_list.append({
            'judul': judul,
            'waktu_rilis': tanggal,
            'tanggal': get_news_date(tanggal)
        })

    with open("data.json", "w") as file:
        json.dump(news_list, file, indent=4)


def get_news_date(data_date):
    # print(data_date)
    split_data_1 = data_date.split("-")
    split_data = split_data_1[1].split()
    # print(split_data)

    value_info = int(split_data[0])
    info = split_data[1]

    # print(f"{value_info} + {info}")

    # print(data_date)
    hari_ini = datetime.now().replace(microsecond=0)
    # print(hari_ini.strftime("%d/%m/%Y %H:%M"))
    # if info.lower() == 'detik':
    #     time = timedelta(seconds=value_info)
    time = None
    if info.lower() == 'menit':
        time = timedelta(minutes=value_info)
    elif info.lower() == 'jam':
        time = timedelta(hours=value_info)
    elif info.lower() == 'hari':
        time = timedelta(days=value_info)

    selisih = hari_ini - time

    # print(f"waktu {selisih.strftime('%Y-%m-%d %H:%M')}")
    return selisih.strftime('%Y-%m-%d %H:%M')


if __name__ == '__main__':
    scraping()



