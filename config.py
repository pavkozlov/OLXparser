import main

PARAMS = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь',
}


def write_head():
    main.write_data({
        'href': 'URL',
        'name': 'НАЗВАНИЕ',
        'cathegory': 'КАТЕГОРИЯ',
        'price': 'ЦЕНА',
        'place': 'ГОРОД',
        'date': 'ДАТА',
        'olxdelivery': 'ДОСТАВКА'
    })


# РЕДАКТИРОВАТЬ ТОЛЬКО ТО, ЧТО НИЖЕ ЭТОЙ СТРОКИ!!!

URL = 'https://www.olx.ua/list/q-iphone-6/'

FILENAME = 'result.csv'

FILDNAMES = ['href', 'name', 'cathegory', 'price', 'place', 'date', 'olxdelivery']
