from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # не понял зачем это делаем?

binary_yandex_driver_file = 'driver/yandexdriver.exe'  # path to YandexDriver

driver = webdriver.Chrome(options=options, service=ChromeService(binary_yandex_driver_file))

driver.get('https://saucedemo.com')
driver.set_window_size(1020, 180)

# driver.quit()
