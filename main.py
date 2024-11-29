import datetime

from faker import Faker
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep
import os

url_base = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)
    sleep(1)

    # Домашнее задание
    # создаём текстовый файл для загрузки
    fake = Faker('ru_RU')
    file_name = fake.text(max_nb_chars=7) + 'pdf'  # поменять на txt для теста ошибки загрузки
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(fake.sentence(nb_words=5))
    file_path = os.path.abspath(file_name)
    # Загружаем файл в браузер и проверяем статус загрузки
    try:
        ibrowser.send_keys_by_xpath('//input[@type="file"]', file_path)
        sleep(1)
        assert ibrowser.value_by_xpath('//div[@id="error"]') == 'File Successfully Uploaded', \
            f'Ошибка загрузки файла: {ibrowser.value_by_xpath('//div[@id="error"]')}\n'
        print(f'Файл "{file_name}" успешно загружен на сайт')
        file_name_in_browser = ibrowser.driver.find_element(By.XPATH, '//input[@type="file"]').get_attribute('value')
        assert file_name_in_browser[-len(file_name):] == file_name, f'Загружен не тот файл!!'
        print('Имя загруженного файла совпадает с исходным')
    except AssertionError as err:
        print(err.args[0])

    # Удаление файла
    os.remove(file_path)
    print(f'Файл "{file_name}" успешно удален')

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
