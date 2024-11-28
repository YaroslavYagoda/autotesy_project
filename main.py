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

url_base = 'https://the-internet.herokuapp.com/javascript_alerts'

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
    tuple_button_locators = ('//button[@onclick="jsAlert()"]',
                            '//button[@onclick="jsConfirm()"]',
                            '//button[@onclick="jsPrompt()"]',)

    # В цикле будут нажаты все кнопки и обработаны все предупреждения с методом .accept()
    for button_locator in tuple_button_locators:
        button_name = ibrowser.value_by_xpath(button_locator)
        ibrowser.click_by_xpath(button_locator)
        print(f'Нажата кнопка "{button_name}"')
        try:
            ibrowser.driver.switch_to.alert.send_keys('Test string')
            print(f'Предупреждению по кнопке "{button_name}" передан текст')
        except Exception:
            pass
        finally:
            ibrowser.driver.switch_to.alert.accept()
            print(f'В предупреждении по кнопке "{button_name}" нажато подтвердить (ОК)\n')
            sleep(2)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
