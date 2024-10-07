from chromebrowser import ChromeBrowser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class FireFox(ChromeBrowser):
    """
    Браузер FireFox - дочерний класс "ChromeBrowser"
    """

    def __init__(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
