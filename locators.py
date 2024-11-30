# Выбор браузера для работы
browser_query = 'Выберите установленный браузер для продолжения работы:'
browser_action = ['1. ChromeBrowser', '2. MsEdge', '3. YaBrowser']

# Адрес сайта
url_base = 'https://www.saucedemo.com/'

# Авторизация на сайте
login = 'standard_user'
login_input = '//input[@id="user-name"]'
password = 'secret_sauce'
password_input = '//input[@id="password"]'
login_button = '//input[@id="login-button"]'

# Страница с продуктами
product_query = 'Выберите один из предложенных товаров:'
product_names = '//div[@class="inventory_item_name "]'
product_buttons = '//button[@class="btn btn_primary btn_small btn_inventory "]'
product_prices = '//div[@class="inventory_item_price"]'

# Корзина
shop_cart_link = '//a[@class="shopping_cart_link"]'
user_product_cart = '//div[@class="inventory_item_name"]'
checkout_button = '//button[@id="checkout"]'

# Данные пользователя
first_name_input = '//input[@id="first-name"]'
last_name_input = '//input[@id="last-name"]'
postal_code_input = '//input[@id="postal-code"]'
continue_button = '//input[@id="continue"]'

# Проверка заказа
summary_subtotal_label = '//div[@class="summary_subtotal_label"]'
finish_button = '//button[@id="finish"]'

# Страница "Заказа оформлен"
complete_label = '//h2[@class="complete-header"]'
back_to_products_button = '//button[@id="back-to-products"]'
