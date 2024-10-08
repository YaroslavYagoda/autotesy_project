from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox

url_base = 'https://saucedemo.com'


url_catalog = 'https://www.saucedemo.com/inventory.html'
element_catalog = 'Products'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser, MsEdge, FireFox)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')
    try:
        # Загрузка сайта
        ibrowser.get_url(url_base)

        # Авторизация на сайте
        ibrowser.send_keys_by_xpath("//input[@id='user-name']", 'standard_user')
        ibrowser.send_keys_by_xpath("//input[@id='password']", 'secret_sauce')
        ibrowser.click_by_xpath("//input[@id='login-button']")
        print('Действия по авторизации выполнены')

        # Проведение тестов
        ibrowser.check_current_url(url_catalog)
        ibrowser.check_by_element_on_page(element_catalog, "//span[@class='title']")

    except AssertionError as err:
        print('\nВозникла ошибка!')
        print('\t', err.args[0], '\n\n')
    else:
        # Информационное сообщение в консоль о завершении
        print(f'\nПроверка для браузера {browser.__name__} проведена успешно\n\n')

    finally:
        # Закрытие браузера
        ibrowser.quit()
