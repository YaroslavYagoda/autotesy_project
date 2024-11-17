from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://demoqa.com/checkbox'
#user = "standard_user"
#password = "secret_sauce"
# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)

    # Выбор и проверка чекбокса
    check_box = ibrowser.driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
    check_box.click()
    if check_box.is_selected():
        print('Чек-бокс выбран')
    else:
        print('Чек-бокс не выбран')
        sleep(2)
    """
    На самом деле локатор '//span[@class="rct-checkbox"]' не даст выбрать какой либо другой чек-бокс
    кроме как первый, выбор локатора в уроке выбран странно я бы сделал по другому (ниже код)
    """
    check_box = ibrowser.driver.find_element(By.XPATH, '//label[@for="tree-node-home"]/span[1]')
    check_box.click()
    if check_box.is_selected():
        print('Чек-бокс выбран')
    else:
        print('Чек-бокс не выбран')
    sleep(2)
    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
