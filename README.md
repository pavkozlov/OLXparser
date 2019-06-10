# OLXparser

Парсер сайта https://www.olx.ua/l

# Инструкция

1) Скачать проект на компьютер
    
2) Установить python 3
    
3) Открыть терминал, с помощью cd перейти в папку с проектом
    
4) Установить библиотеки с помощью пакетного менеджера pip pip install -r requirements.txt
    
5) В файле config.py (открыв его любым текстовым редактором, например блокнотом) изменить URL (что мы будем парсить?). 

5.1) Примеры URL: 
https://www.olx.ua/list/q-авто/ 
https://www.olx.ua/list/q-нарды/ 
https://www.olx.ua/list/q-шахматы/ 
https://www.olx.ua/list/q-прохладительные_напитки/ 
https://www.olx.ua/list/q-apple/
    
6) Если необходимо, в этом же файле изменить FILENAME (название создаваемого файла) и FILDNAMES (в каком порядке будут распологаться поля). Можно оставить эти значения по умолчанию.
    
7) Выполнить в терминале команду, находясь в папке проекта python main.py
    
8) Дождаться появления CSV файла в текущей дирректории
