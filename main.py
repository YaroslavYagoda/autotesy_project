import time
from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox

url = 'https://saucedemo.com'

# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки меняй на тот который у тебя (для этого импортировал все классы)
ibrowser = MsEdge()

ibrowser.get_url(url)

ibrowser.send_keys_by_id('user-name', 'standard_user')
ibrowser.send_keys_by_id('password', 'secret_sauce')
# time.sleep(5)
# ibrowser.quit()
