from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep
from selenium.webdriver.common.keys import Keys

url_base = 'https://saucedemo.com'
url_catalog = 'https://www.saucedemo.com/inventory.html'
element_catalog = 'Products'
user_tuple = ('standard_user', 'locked_out_user', '')
password_tuple = ('secret_sauce', 'wrong_password', '')

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser, MsEdge)

# Сначала проверка для действительного пароля для всех юзеров (и пустого)
# Затем для некорректного пароля и пустого
for password in password_tuple:
    for user in user_tuple:
        print(f'{'*' * 30}\n\nЛогин:\n\t{user}\nПароль:\n\t{password}\n\n')
        for browser in browser_tuple:
            ibrowser = browser()
            print(f'Начало проверки для браузера {browser.__name__}\n')
            try:
                # Загрузка сайта
                ibrowser.get_url(url_base)

                # ВВод логина и пароля для дальнейшей работы
                # ibrowser.send_keys_by_xpath("//input[@id='user-name']", user)
                # ibrowser.send_keys_by_xpath("//input[@id='password']", password)
                # sleep(2)

                # Имитация нажатия клавиш
                # ibrowser.send_keys_by_xpath("//input[@id='user-name']", Keys.CONTROL + 'a')
                # sleep(2)
                # ibrowser.send_keys_by_xpath("//input[@id='user-name']", Keys.BACKSPACE)
                # sleep(1)

                # Вариант без импорта Keys
                # ibrowser.send_keys_by_xpath("//input[@id='password']", '\ue009 a')
                # sleep(2)
                # ibrowser.send_keys_by_xpath("//input[@id='password']", '\ue003')
                # sleep(3)

                # Авторизация на сайте
                ibrowser.send_keys_by_xpath("//input[@id='user-name']", user)
                ibrowser.send_keys_by_xpath("//input[@id='password']", password)
                ibrowser.send_keys_by_xpath("//input[@id='password']", Keys.ENTER)
                # ibrowser.click_by_xpath("//input[@id='login-button']")
                # проверка на наличия контейнера с ошибкой и вывод ее текста
                ibrowser.check_element_and_his_null_text("//div[@class='error-message-container error']")
                # не стал добавлять клик по крестику ibrowser.click_by_xpath("//button[@class='error-button']")
                # тем более при вызове исключения метод не сработает или не будет проверенно исключение
                print('Авторизация на сайте проведена')

                # Проведение тестов
                ibrowser.check_current_url(url_catalog)
                ibrowser.check_by_element_on_page(element_catalog, "//span[@class='title']")

            except AssertionError as err:
                print('❌Возникла ошибка!\n\t', err.args[0], '\n')
            else:
                # Информационное сообщение в консоль о завершении
                print(f'\n✅Проверка для браузера {browser.__name__} проведена успешно')

            finally:
                # Скриншот в media_report/*
                sleep(2)
                screenshot_name = f'{browser.__name__}.{user}.{password}'
                ibrowser.make_scrinshot(screenshot_name)

                # Закрытие браузера
                ibrowser.quit()
                print(f'Процесс браузера {browser.__name__} завершен\n\n')
