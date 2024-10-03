from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=options, service=ChromeService(ChromeDriverManager().install()))

    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def send_keys_by_id(self, valueID: str, data: str):
        field = self.driver.find_element(By.ID, valueID)
        field.send_keys(data)
