from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


class ChromeBrowser:
    """
    Браузер Chrome - родительский класс для других браузеров
    """

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    def get_url(self, url: str):
        """
        Переход на страницу c адресом "url",
        размер окна браузера по размеру экрана
        :param url: адрес страницы в текстовом формате
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def quit(self):
        """
        Закрытие браузера
        """
        self.driver.quit()

    def send_keys_by_id(self, valueID: str, data: str):
        """
        Ввод текстовой информации "data" в элемент на странице по его "valueID"
        :param valueID: ID элемента на странице
        :param data: вводимая текстовая информация
        """
        field = self.driver.find_element(By.ID, valueID)
        field.send_keys(data)

    def send_keys_by_xpath(self, xpath: str, data: str):
        """
        Ввод текстовой информации "data" в элемент на странице по его "xpath"
        :param xpath: XPATH элемента на странице
        :param data: вводимая текстовая информация
        """
        field = self.driver.find_element(By.XPATH, xpath)
        field.send_keys(data)

    def click_by_xpath(self, xpath: str, ):
        """
        Эмуляция нажатия(click) на элемент страницы по его "xpath"
        :param xpath: XPATH элемента на странице
        """
        field = self.driver.find_element(By.XPATH, xpath)
        field.click()

    def check_current_url(self, url_check: str):
        """
        Проверка соответствия адреса текущей страницы браузера контрольному "url_check"
        :param url_check: контрольный адрес страницы
        """
        assert url_check == self.driver.current_url, (f'Текущая страница браузера не соответствует контрольной '
                                                      f'"{url_check}"')
        print(f'Текущая страница браузера соответствует контрольной "{url_check}".\n\tПроверка проведена успешно')

    def check_by_element_on_page(self, check_element: str, xpath: str):
        """
        Проверка наличия контрольного элемента (по названию) "check_element" на странице по его "xpath"
        :param check_element: название контрольного элемента страницы
        :param xpath: XPATH элемента на странице
        :return:
        """
        assert check_element == self.driver.find_element(By.XPATH, xpath).text, (f'Контрольный элемент '
                                                                                 f'{check_element} не найден')
        print(f'Проверка наличия контрольного элемента "{check_element}" проведена успешно')

    def check_element_and_his_null_text(self, xpath: str):
        try:
            text = self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            pass
        else:
            assert text == '', text

    def make_scrinshot(self, screenshot_name: str):
        now = datetime.now().strftime('%d.%m.%Y, %H.%M.%S')
        self.driver.save_screenshot(f'media_report/{screenshot_name} {now}.png')
        print('Скриншот сохранен!')
