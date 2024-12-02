from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox

from faker import Faker
from time import sleep
from locators import *
from os import system

# Кортеж доступных браузеров
tuple_of_browser = (ChromeBrowser, MsEdge, YaBrowser)


def choice_of_answer(query, list_of_action):
    """
    Функция для выбора одного варианта из списка предложенных
    :param query: str - Вопрос пользователю
    :param list_of_action: Список(кортеж) с вариантами ответов (номера ответов проставляются автоматически с 1)
    :return: номер выбранного варианта
    """
    choice = ''
    list_of_answer = [str(i + 1) for i in range(len(list_of_action))]
    while choice not in list_of_answer:
        system('cls||clear')
        print(query)
        for action in list_of_action:
            print('\t' + action)
        choice = input()
    return int(choice)


def choice_browser():
    """
    Возвращает класс браузера из кортежа с браузерами
    :return: Browser
    """
    return tuple_of_browser[choice_of_answer(browser_query, browser_action) - 1]


class SmokeTestSwagLabs():
    """
    Класс с тестами в виде методов
    """
    def __init__(self, browser):
        self.ibrowser = browser()

    def test1(self):
        """
        Метод для SmokeTest сайта "Swag Labs"
        """
        print('Ожидайте загрузки товаров....🔁')
        # Загрузка сайта
        self.ibrowser.get_url(url_base)
        WebDriverWait(self.ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, login_button)))

        # Авторизация на сайте
        self.ibrowser.send_keys_by_xpath(login_input, login)
        self.ibrowser.send_keys_by_xpath(password_input, password)
        self.ibrowser.click_by_xpath(login_button)

        # Получение товара и предложение его пользователю + выбор
        WebDriverWait(self.ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, shop_cart_link)))
        list_product = self.ibrowser.driver.find_elements(By.XPATH, product_names)
        product_user_choice = choice_of_answer(product_query,
                                               [str(i + 1) + '. ' + list_product[i].text for i in
                                                range(len(list_product))]) - 1
        user_product_name = list_product[product_user_choice].text
        user_product_price = self.ibrowser.driver.find_elements(By.XPATH, product_prices)[product_user_choice].text[-5:]

        # Добавление товара в корзину
        self.ibrowser.driver.find_elements(By.XPATH, product_buttons)[product_user_choice].click()

        # Проверка товара в корзине
        self.ibrowser.click_by_xpath(shop_cart_link)
        WebDriverWait(self.ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, checkout_button)))
        assert user_product_name == self.ibrowser.value_by_xpath(
            user_product_cart), 'Ошибка!! В корзину добавлен иной продукт'
        assert user_product_price == self.ibrowser.value_by_xpath(product_prices)[
                                     -5:], 'Ошибка!! Цена в корзине отличается'

        # Создание данных на покупателя (фейковых)
        fake = Faker('en_US')
        first_name = fake.first_name()
        last_name = fake.last_name()
        postal_code = fake.postalcode()

        # Внесение данных покупателя в форму
        self.ibrowser.click_by_xpath(checkout_button)
        WebDriverWait(self.ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, continue_button)))
        self.ibrowser.send_keys_by_xpath(first_name_input, first_name)
        self.ibrowser.send_keys_by_xpath(last_name_input, last_name)
        self.ibrowser.send_keys_by_xpath(postal_code_input, postal_code)

        # Проверка оформленного товара
        self.ibrowser.click_by_xpath(continue_button)
        WebDriverWait(self.ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, finish_button)))
        assert user_product_name == self.ibrowser.value_by_xpath(user_product_cart), 'Ошибка!! В заказе иной продукт'
        assert user_product_price == self.ibrowser.value_by_xpath(summary_subtotal_label)[
                                     -5:], 'Ошибка!! Цена в заказе отличается'

        # Завершение оформления товара и возврат в раздел покупок
        self.ibrowser.click_by_xpath(finish_button)
        WebDriverWait(self.ibrowser.driver, 10).until(ES.element_to_be_clickable(
            (By.XPATH, back_to_products_button)))
        assert 'Thank you for your order!' == self.ibrowser.value_by_xpath(complete_label), 'Ошибка формирования заказа'
        self.ibrowser.click_by_xpath(back_to_products_button)
        print(
            f'\nВаш товар "{user_product_name}" оформлен, не забудьте покормить морковкой Пони,'
            f'которая привезет вам его😀')

        # Завершение работы браузера
        self.ibrowser.quit()
