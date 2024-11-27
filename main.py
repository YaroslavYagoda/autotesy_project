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

url_base = 'https://www.saucedemo.com/'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)
    sleep(1)

    # Домашнее задание
    # Подготовка исходных данных
    user_name_locator = '//input[@id="user-name"]'
    fake = Faker('en_US')
    fake_name = fake.first_name()
    print(f'Создано фейковое имя: {fake_name}')

    # Ввод данных фейковых данных
    ibrowser.send_keys_by_xpath(user_name_locator, fake_name)
    print('Фейковое имя введенов строку логина')
    sleep(2)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
