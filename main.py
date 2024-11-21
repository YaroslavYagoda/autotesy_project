import datetime
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://html5css.ru/howto/howto_js_rangeslider.php'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')

    # Загрузка сайта
    ibrowser.get_url(url_base)
    sleep(0.5)
    # Домашнее задание
    action = ActionChains(ibrowser.driver)
    slider = ibrowser.driver.find_element(By.XPATH, '//input[@class="slider-color"]')

    # Получение атрибутов значения слайдера для определения шага в пиксилях для одной единицы
    current_value = int(slider.get_attribute('value'))

    # Поиск шага в пикселях для одной единицы и поправки для увеличения
    slider_value = ibrowser.driver.find_element(By.XPATH, '//span[@id="f"]')
    pixel_step = 0
    koff = 0

    # поправка
    while int(slider_value.text) == current_value:
        koff += 1
        action.click_and_hold(slider).move_by_offset(koff, 0).release().perform()

    # возврат на исходную позицию
    action.click_and_hold(slider).move_by_offset(0, 0).release().perform()

    # шаг
    while int(slider_value.text) == current_value:
        pixel_step += 1
        action.click_and_hold(slider).move_by_offset(-pixel_step, 0).release().perform()

    print(f'Шаг для 1 ед. = {pixel_step},поправка - {koff}')

    # Проверка правильности шага и поправки для значения 38 и 61
    action.click_and_hold(slider).move_by_offset(pixel_step * (-12), 0).release().perform()
    assert int(slider_value.text) == 38, f'Значение ползунка - {slider_value.text} должно быть 38!'

    action.click_and_hold(slider).move_by_offset(pixel_step * 11 - koff, 0).release().perform()
    assert int(slider_value.text) == 61, f'Значение ползунка - {slider_value.text} должно быть 61!'

    print('Шаг проверен')
    sleep(1)

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
