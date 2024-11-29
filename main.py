import datetime

from faker import Faker
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep
import os

url_base = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
path_for_download = os.path.dirname(os.path.abspath(__file__)) + '\\downloads'
file_name = path_for_download + '\\' + 'LambdaTest.pdf'
file_size = 100
# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)
    sleep(1)

    # Загрузка файла
    ibrowser.click_by_xpath('//button[@class="btn btn-primary"]')

    # Проверка загрузки файла
    wait_seс = 0
    while not os.access(file_name, os.F_OK) and wait_seс < 10:
        sleep(1)
        wait_seс += 1

    assert os.access(file_name, os.F_OK), \
        'Ошибка загрузки файла'
    print('Файл загружен')

    assert os.path.getsize(file_name) > file_size, \
        'Размер файла не соответствует контрольному размеру'
    print('Файл, предположительно, загружен полностью')

    # Удаление загруженного файла
    os.remove(file_name)
    print('Файл удален\n')

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
