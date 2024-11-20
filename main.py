import datetime
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://demoqa.com/date-picker'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)

    # Домашнее задание
    ibrowser.send_keys_by_xpath('//input[@id="datePickerMonthYearInput"]', Keys.CONTROL + 'A')
    ibrowser.send_keys_by_xpath('//input[@id="datePickerMonthYearInput"]', Keys.DELETE)

    current_data = datetime.datetime.now() + datetime.timedelta(days=10)
    # На видео в уроке указан не правильный формат вывода даты
    current_data = current_data.strftime('%m/%d/%y')

    ibrowser.send_keys_by_xpath('//input[@id="datePickerMonthYearInput"]', current_data)
    sleep(2)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
