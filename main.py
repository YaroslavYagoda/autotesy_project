from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common import exceptions as Sel_exsept

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox

from time import sleep

url_base = 'https://demoqa.com/dynamic-properties'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)
    sleep(3)

    # Домашняя работа
    wait_sec = 0
    max_sec = 2
    check = False
    while not check and wait_sec < max_sec:
        try:
            ibrowser.click_by_xpath('//button[@id="visibleAfter"]')
        except Sel_exsept.NoSuchElementException as err:
            print(f'Попытка № {wait_sec+1}. Возникла ошибка {err.__class__.__name__}.')
        else:
            check = True
            print(f'Попытка № {wait_sec+1}. Кнопка нажата')
        finally:
            wait_sec += 1
            sleep(1)
    if wait_sec == max_sec:
        print('Элемент не был обнаружен. Лимит попыток исчерпан')

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
