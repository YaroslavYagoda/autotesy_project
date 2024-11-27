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

url_base = 'https://demoqa.com/browser-windows'

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
    ibrowser.click_by_xpath('//button[@id="tabButton"]')
    ibrowser.driver.switch_to.window(ibrowser.driver.window_handles[1])
    assert ibrowser.value_by_xpath('//h1[@id="sampleHeading"]') == 'This is a sample page', \
        f'Проверка перехода не пройдена'
    print('Проверка создания и перехода на новую вкладку пройдена')
    sleep(1)
    # Переключение на предыдущую вкладку
    ibrowser.driver.switch_to.window(ibrowser.driver.window_handles[0])

    # Новое окно
    ibrowser.click_by_xpath('//button[@id="windowButton"]')
    # странно что в уроке никто не отметил что все вкладки и окна идут в едином списке
    # driver.window_handles, и если не закрыть вкладку, то новое окно третье по счету, а не второе
    ibrowser.driver.switch_to.window(ibrowser.driver.window_handles[2])
    sleep(1)
    assert ibrowser.value_by_xpath('//h1[@id="sampleHeading"]') == 'This is a sample page', \
        f'Проверка перехода не пройдена'
    print('Проверка создания и перехода на новое окно пройдена')
    # Переключение на предыдущую вкладку
    ibrowser.driver.switch_to.window(ibrowser.driver.window_handles[0])
    sleep(3)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
