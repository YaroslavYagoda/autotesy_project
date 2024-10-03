from chromebrowser import ChromeBrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class YaBrowser(ChromeBrowser):
    def __init__(self):
        binary_yandex_driver_file = 'driver/yandexdriver.exe'
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options, service=ChromeService(binary_yandex_driver_file))