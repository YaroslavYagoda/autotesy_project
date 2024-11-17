from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://demoqa.com/buttons'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)

    # Домашнее задание
    double_click_btn = ibrowser.driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
    right_click_btn = ibrowser.driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')

    action = ActionChains(ibrowser.driver)
    action.double_click(double_click_btn).perform()
    print('double_click_btn')
    action.context_click(right_click_btn).perform()
    print('right_click_btn')


    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
