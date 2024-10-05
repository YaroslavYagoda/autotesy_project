import time
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox

url = 'https://saucedemo.com'
# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser, MsEdge, FireFox)

for browser in browser_tuple:
    ibrowser = browser()

    # Загрузка сайта
    ibrowser.get_url(url)

    # Авторизация на сайте
    ibrowser.send_keys_by_xpath("//input[@id='user-name']", 'standard_user')
    ibrowser.send_keys_by_xpath("//input[@id='password']", 'secret_sauce')
    ibrowser.click_by_xpath("//input[@id='login-button']")
    time.sleep(5)
    # Закрытие браузера
    ibrowser.quit()

    # Информационное сообщение в консоль
    print(f'Авторизация через браузер {browser.__name__} проведена')