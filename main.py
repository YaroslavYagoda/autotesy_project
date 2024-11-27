import datetime
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'

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
    # Переключение на вложенный контейнер
    iframe = ibrowser.driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
    ibrowser.driver.switch_to.frame(iframe)

    # Подготовка исходных данных
    text_box_locator = '//div[@class="rsw-ce"]'
    text_input = 'Test message'
    button_bold_locator = '//button[@title="Bold"]'
    button_italic_locator = '//button[@title="Italic"]'

    # Вdод текста в поле и проверка корректности ввода
    ibrowser.send_keys_by_xpath(text_box_locator, Keys.CONTROL+"A")
    ibrowser.send_keys_by_xpath(text_box_locator, Keys.DELETE)
    ibrowser.send_keys_by_xpath(text_box_locator, text_input)
    text_result = ibrowser.value_by_xpath(text_box_locator)
    assert text_input == text_result, f'Ожидается:{text_input}, получено: {text_result} '
    print('Текст введен корректно')
    sleep(0.2)

    # Редактирование текста и проверка его корректности после изменений
    ibrowser.send_keys_by_xpath(text_box_locator, Keys.CONTROL + "A")
    ibrowser.click_by_xpath(button_bold_locator)
    ibrowser.click_by_xpath(button_italic_locator)
    text_result = ibrowser.value_by_xpath(text_box_locator)
    assert text_input == text_result, f'Ожидается:{text_input}, получено: {text_result} '
    print('Текст после изменения внешнего вида корректен')
    sleep(2)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
