import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.edge.service import Service as MsEdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

binary_yandex_driver_file = 'driver/yandexdriver.exe'
url = 'https://saucedemo.com'

# Запуск Яндекс браузера с ручным обновлением драйвера
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=ChromeService(binary_yandex_driver_file))

driver.get(url)
driver.maximize_window()
time.sleep(5)
driver.quit()  # завершить браузер как процесс
# driver.close() ???закрыть активную вкладку или окно???

# Запуск MicrosoftEdge с автообновлением драйвера
options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=options, service=MsEdgeService(EdgeChromiumDriverManager().install()))

driver.get(url)
driver.maximize_window()
time.sleep(5)
driver.quit()

# Запуск FireFox c автообновлением драйвера
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://saucedemo.com')
driver.maximize_window()
time.sleep(5)
driver.quit()
