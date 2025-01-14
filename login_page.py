from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

from chromebrowser import ChromeBrowser

# Импортирую все локаторы, логин и пароль, которые при необходимости можно переопределить в коде
from locators import *


class LoginPage(ChromeBrowser):
    """
    Класс для авторизации
    """
    def __init__(self, ibrowser):
        self.ibrowser = ibrowser

    def authorithation(self, login=login, password=password):
        """
        Авторизация на сайте
        :param login: по умолчанию из locators
        :param password: по умолчанию из locators
        """
        WebDriverWait(self.ibrowser.driver, 10).until(ES.element_to_be_clickable((By.XPATH, login_button)))
        self.ibrowser.send_keys_by_xpath(login_input, login)
        self.ibrowser.send_keys_by_xpath(password_input, password)
        self.ibrowser.click_by_xpath(login_button)
        print(f'Авторизация с логином "{login}" и паролем "{password}" проведена')
