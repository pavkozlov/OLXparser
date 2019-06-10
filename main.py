import re
import bs4
import requests
import csv
from datetime import datetime

import config
import time


def get_html(url):
    r = requests.get(url)
    return r.text if re.search(config.URL, r.url) else None


def get_data(html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='offers_table').findAll('tr', class_='wrap')

    for tr in trs:
        try:
            price = tr.find('p', class_='price').find('strong').text
        except AttributeError:
            price = 'Не указано'

        delivery = tr.find('div', class_='olx-delivery-badge__suggest hidden')

        data = {
            'href': tr.find('a').get('href'),
            'name': clean_name(tr.find('strong').text),
            'date': clean_date(tr.find('td', valign="bottom").findAll('span')[1].text.strip()),
            'place': tr.find('td', valign="bottom").findAll('span')[0].text.strip(),
            'cathegory': tr.find('small', class_='breadcrumb x-normal').text.strip(),
            'price': clean_price(price),
            'olxdelivery': True if delivery else False

        }

        write_data(data)


def clean_price(price):
    if price == 'Не указано' or price == 'Обмен':
        return price
    else:
        result = re.search('(.*) грн.', price).group(1)
        return result.replace(' ', '')


def clean_date(publications_date):
    res = re.search('(.*) \d{2}:\d{2}', publications_date)

    if res and res.group(1) == 'Сегодня':
        date = f'{datetime.today().day} {config.PARAMS[datetime.today().month]}'
        return date
    elif res and res.group(1) == 'Вчера':
        date = f'{datetime.today().day - 1} {config.PARAMS[datetime.today().month]}'
        return date
    else:
        return publications_date


def clean_name(name):
    return name.replace(',', ' ').replace(';', ' ')


def write_data(data):
    with open(config.FILENAME, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=config.FILDNAMES)
        writer.writerow(data)


def main():
    config.write_head()
    url = config.URL
    page = 1

    while True:

        try:
            html = get_html(f'{url}?page={page}')
            if html:
                get_data(html)
                page += 1
            else:
                break

        except AttributeError:
            time.sleep(1)
            html = get_html(url)
            if html:
                get_data(html)
                page += 1
            else:
                break


if __name__ == '__main__':
    main()
