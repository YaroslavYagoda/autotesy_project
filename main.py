from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://saucedemo.com'
user = "standard_user"
password = "secret_sauce"
# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')
    # Загрузка сайта
    ibrowser.get_url(url_base)

    # Авторизация на сайте
    ibrowser.send_keys_by_xpath("//input[@id='user-name']", user)
    ibrowser.send_keys_by_xpath("//input[@id='password']", password)
    ibrowser.send_keys_by_xpath("//input[@id='password']", Keys.ENTER)

    # переход в корзину
    ibrowser.click_by_xpath("//a[@class='shopping_cart_link']")

    # Домашнее задание
    sleep(1)
    ibrowser.driver.back()
    sleep(1)
    ibrowser.driver.forward()

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
