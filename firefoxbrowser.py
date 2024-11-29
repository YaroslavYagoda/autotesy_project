import os

from chromebrowser import ChromeBrowser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class FireFox(ChromeBrowser):
    """
    Браузер FireFox - дочерний класс "ChromeBrowser"
    """

    def __init__(self):
        options = webdriver.FirefoxOptions()
        path_for_download = os.path.dirname(os.path.abspath(__file__)) + '\\downloads'
        prefs = {'download.default_directory': path_for_download}
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
        self.create_download_dir()