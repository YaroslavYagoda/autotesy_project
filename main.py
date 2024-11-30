from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions as Sel_exsept

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox

from faker import Faker
from time import sleep
from locators import *
from os import system

tuple_of_browser = (ChromeBrowser, MsEdge, YaBrowser)


def choice_of_answer(query, list_of_action):
    choice = ''
    list_of_answer = [str(i + 1) for i in range(len(list_of_action))]
    while choice not in list_of_answer:
        system('cls||clear')
        print(query)
        for action in list_of_action:
            print('\t' + action)
        choice = input()
    return int(choice)


# Выбор браузера для работы
ibrowser = tuple_of_browser[choice_of_answer(browser_query, browser_action) - 1]()
print('Ожидайте загрузки товаров....🔁')

# Загрузка сайта
ibrowser.get_url(url_base)
WebDriverWait(ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, login_button)))

# Авторизация на сайте
ibrowser.send_keys_by_xpath(login_input, login)
ibrowser.send_keys_by_xpath(password_input, password)
ibrowser.click_by_xpath(login_button)

# Получение товара и предложение его пользователю + выбор
WebDriverWait(ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, shop_cart_link)))
list_product = ibrowser.driver.find_elements(By.XPATH, product_names)
product_user_choice = choice_of_answer(product_query,
                                       [str(i + 1) + '. ' + list_product[i].text for i in range(len(list_product))]) - 1
user_product_name = list_product[product_user_choice].text
user_product_price = ibrowser.driver.find_elements(By.XPATH, product_prices)[product_user_choice].text[-5:]

# Добавление товара в корзину
ibrowser.driver.find_elements(By.XPATH, product_buttons)[product_user_choice].click()

# Проверка товара в корзине
ibrowser.click_by_xpath(shop_cart_link)
WebDriverWait(ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, checkout_button)))
assert user_product_name == ibrowser.value_by_xpath(user_product_cart), 'Ошибка!! В корзину добавлен иной продукт'
assert user_product_price == ibrowser.value_by_xpath(product_prices)[-5:], 'Ошибка!! Цена в корзине отличается'

# Создание данных на покупателя (фейковых)
fake = Faker('en_US')
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postalcode()

# Внесение данных покупателя в форму
ibrowser.click_by_xpath(checkout_button)
WebDriverWait(ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, continue_button)))
ibrowser.send_keys_by_xpath(first_name_input, first_name)
ibrowser.send_keys_by_xpath(last_name_input, last_name)
ibrowser.send_keys_by_xpath(postal_code_input, postal_code)

# Проверка оформленного товара
ibrowser.click_by_xpath(continue_button)
WebDriverWait(ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, finish_button)))
assert user_product_name == ibrowser.value_by_xpath(user_product_cart), 'Ошибка!! В заказе иной продукт'
assert user_product_price == ibrowser.value_by_xpath(summary_subtotal_label)[-5:], 'Ошибка!! Цена в заказе отличается'

# Завершение оформления товара и возврат в раздел покупок
ibrowser.click_by_xpath(finish_button)
WebDriverWait(ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, back_to_products_button)))
assert 'Thank you for your order!' == ibrowser.value_by_xpath(complete_label), 'Ошибка формирования заказа'
ibrowser.click_by_xpath(back_to_products_button)
print(f'\nВаш товар "{user_product_name}" оформлен, не забудьте покормить морковкой Пони, которая привезет вам его😀')

# Завершение работы браузера
ibrowser.quit()
