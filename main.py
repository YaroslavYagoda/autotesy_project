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

# Сначала проверка для действительного пароля для всех юзеров (и пустого)
# Затем для некорректного пароля и пустого
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
                ibrowser.send_keys_by_xpath("//input[@id='password']", "\ue007")

                # проверка на наличия контейнера с ошибкой и вывод ее текста
                ibrowser.check_element_and_his_null_text("//div[@class='error-message-container error']")
                print('Авторизация на сайте проведена')

                # Проведение тестов
                ibrowser.check_current_url(url_catalog)
                ibrowser.check_by_element_on_page(element_catalog, "//span[@class='title']")

                # добавление товаров в корзину
                products = ibrowser.get_elements_as_list_by_xpath("//div[@class='inventory_item_name ']")
                buttons = (ibrowser.get_elements_as_list_by_xpath(
                    "//button[@class='btn btn_primary btn_small btn_inventory ']"))
                assert len(products) == len(buttons), 'Количество товаров и кнопок добавить товар не совпадает'

                print('Добавление товаров в корзину:\n')
                for counter in range(len(products)):
                    buttons[counter].click()
                    print(f'\tТовар "{products[counter].text}" добавлен в корзину')
                print(f'\n\tВсего добавлено в корзину наименований: {len(products)}')

                # переход в корзину
                ibrowser.click_by_xpath("//a[@class='shopping_cart_link']")

                # пролистывание до последней позиции
                products_in_cart = ibrowser.get_elements_as_list_by_xpath("//div[@class='cart_item']")
                ibrowser.scroll_to_element(products_in_cart[-1])

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
