from selenium.webdriver import Keys

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://saucedemo.com'
url_catalog = 'https://www.saucedemo.com/inventory.html'
element_catalog = 'Products'
user_tuple = ('standard_user',)
password_tuple = ('secret_sauce',)

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for password in password_tuple:
    for user in user_tuple:
        print(f'{'*' * 30}\n\nЛогин:\n\t"{user}"\nПароль:\n\t"{password}"\n\n')
        for browser in browser_tuple:
            ibrowser = browser()
            print(f'Начало проверки для браузера {browser.__name__}\n')
            try:
                # Загрузка сайта
                ibrowser.get_url(url_base)

                # Авторизация на сайте
                ibrowser.send_keys_by_xpath("//input[@id='user-name']", user)
                ibrowser.send_keys_by_xpath("//input[@id='password']", password)
                ibrowser.send_keys_by_xpath("//input[@id='password']", Keys.ENTER)

                # Выход с сайта
                ibrowser.click_by_xpath("//button[@id='react-burger-menu-btn']")
                sleep(1)
                ibrowser.click_by_xpath("//a[@id='logout_sidebar_link']")

            except AssertionError as err:
                print('❌Возникла ошибка!\n\t', err.args[0], '\n')

            except Exception as err:
                print(err)

            else:
                # Информационное сообщение в консоль о завершении
                print(f'\n✅Проверка для браузера {browser.__name__} проведена успешно')

            finally:
                # Скриншот в media_report/*
                sleep(2)
                screenshot_name = f'{browser.__name__}.{user}.{password}'
                ibrowser.make_screenshot(screenshot_name)

                # Закрытие браузера
                ibrowser.quit()
                print(f'Процесс браузера {browser.__name__} завершен\n\n')
