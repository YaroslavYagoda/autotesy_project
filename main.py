from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from chromebrowser import ChromeBrowser
from yandexbrowser import YaBrowser
from msedgebrowser import MsEdge
from firefoxbrowser import FireFox
from time import sleep

url_base = 'https://saucedemo.com'
user = "standard_user"
password = "secret_sauce"
# родитель: класс ChromeBrowser, дочки: YaBrowser(ручное обновление), MsEdge, FireFox
# для проверки оставь в кортеже те который есть у тебя (для этого импортировал все классы)
browser_tuple = (YaBrowser,)

for browser in browser_tuple:
    ibrowser = browser()
    print(f'Начало проверки для браузера {browser.__name__}\n')
    # Загрузка сайта
    ibrowser.get_url(url_base)

    # Авторизация на сайте
    ibrowser.send_keys_by_xpath("//input[@id='user-name']", user)
    ibrowser.send_keys_by_xpath("//input[@id='password']", password)
    ibrowser.send_keys_by_xpath("//input[@id='password']", Keys.ENTER)

    # добавление товаров в корзину
    products = ibrowser.driver.find_elements(By.XPATH, "//div[@class='inventory_item']")
    buttons = ibrowser.driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
    products_info = []
    print('Добавление товаров в корзину:')
    for counter in range(2, 4):
        price = products[counter].find_element(By.XPATH, ".//div[@class='inventory_item_price']").text
        name = products[counter].find_element(By.XPATH, ".//div[@class='inventory_item_name ']").text
        products_info.append([name, price])
        buttons[counter].click()
        print(f'\tТовар "{name}" добавлен в корзину')
    print(f'Добавлено в корзину товаров: {len(products_info)}')

    # переход в корзину
    ibrowser.click_by_xpath("//a[@class='shopping_cart_link']")
    products_in_cart = ibrowser.driver.find_elements(By.XPATH, "//div[@class='cart_item']")
    for counter in range(len(products_info)):
        assert (products_info[counter][0] ==
                products_in_cart[counter].find_element(By.XPATH, ".//div[@class='inventory_item_name']").text), \
            f'Наименование товара в корзине под номером {counter + 1} не верное'
        assert (products_info[counter][1] ==
                products_in_cart[counter].find_element(By.XPATH, ".//div[@class='inventory_item_price']").text), \
            f'Цена товара в корзине под номером {counter + 1} не верная'
    print('Товар в корзине проверен')

    # Оформление покупки (ввод данных покупателя)
    ibrowser.click_by_xpath("//button[@class='btn btn_action btn_medium checkout_button ']")
    ibrowser.send_keys_by_xpath("//input[@id='first-name']", "111")
    ibrowser.send_keys_by_xpath("//input[@id='last-name']", "111")
    ibrowser.send_keys_by_xpath("//input[@id='postal-code']", "5658")
    ibrowser.click_by_xpath("//input[@id='continue']")
    print('Сведения о покупателе внесены')

    # Финальная проверка товара
    products_in_cart = ibrowser.driver.find_elements(By.XPATH, "//div[@class='cart_item']")
    for counter in range(len(products_info)):
        assert (products_info[counter][0] ==
                products_in_cart[counter].find_element(By.XPATH, ".//div[@class='inventory_item_name']").text), \
            f'Наименование товара под номером {counter + 1} на странице оформления товара не верное'
        assert (products_info[counter][1] ==
                products_in_cart[counter].find_element(By.XPATH, ".//div[@class='inventory_item_price']").text), \
            f'Цена товара под номером {counter + 1} на странице оформления товара не верная'
    print('Товар на странице оформления товара проверен')

    # Проверка итоговой цены
    total_price = ibrowser.driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']").text
    summary_price_products = f'Item total: ${sum([float(i[1][1:]) for i in products_info])}'
    assert summary_price_products == total_price, 'Итоговая сумма всех товаров неверная'
    print('Итоговая сумма товаров (без налога) проверена')

    # Проверка успешного оформления заказа
    ibrowser.click_by_xpath("//button[@id='finish']")
    ibrowser.check_by_element_on_page("Thank you for your order!", "//h2[@class='complete-header']")

    # Завершение работы браузера
    ibrowser.quit()
    print(f'Процесс браузера {browser.__name__} завершен\n\n')
