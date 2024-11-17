from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://demoqa.com/radio-button'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)

    # Домашнее задание
    radio_button_1 = ibrowser.driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    radio_button_2 = ibrowser.driver.find_element(By.XPATH, '//label[@for="impressiveRadio"]')

    radio_button_1.click()
    print(f'Переключатель один статус нажатия: {radio_button_1.find_element(By.XPATH, '..//input[1]').is_selected()}')
    print(f'Переключатель два статус нажатия: {radio_button_2.find_element(By.XPATH, '..//input[1]').is_selected()}')
    sleep(2)

    radio_button_2.click()
    print(f'Переключатель один статус нажатия: {radio_button_1.find_element(By.XPATH, '..//input[1]').is_selected()}')
    print(f'Переключатель два статус нажатия: {radio_button_2.find_element(By.XPATH, '..//input[1]').is_selected()}')
    sleep(2)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
