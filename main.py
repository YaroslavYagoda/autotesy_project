import datetime
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://www.lambdatest.com/selenium-playground/simple-form-demo '

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)
    sleep(0.5)

    # Домашнее задание часть 1
    text_input = 'Test message'
    ibrowser.send_keys_by_xpath('//input[@id="user-message"]', text_input)
    ibrowser.click_by_xpath('//button[@id="showInput"]')
    text_result = ibrowser.value_by_xpath('//p[@id="message"]')
    assert text_result == text_input, f'Получен ответ{text_result}, ожидается {text_input}'
    print('Проверка 1 пройдена')
    sleep(2)

    # Домашнее задание часть 2
    value_1 = 5
    value_2 = 7
    ibrowser.send_keys_by_xpath('//input[@id="sum1"]', str(value_1))
    ibrowser.send_keys_by_xpath('//input[@id="sum2"]', str(value_2))
    ibrowser.click_by_xpath('//button[@class="mt-20 mb-10 bg-lambda-900 hover:bg-transparent hover:text-lambda-900'
                            ' border border-lambda-900 text-white rounded p-10 focus:outline-none w-180 "]')
    sum_result = ibrowser.value_by_xpath('//p[@id="addmessage"]')
    assert sum_result == str(value_1 + value_2), f'Получент результат:{sum_result}, ожидается {value_1 + value_2}'
    print('Проверка 2 пройдена')
    sleep(2)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
