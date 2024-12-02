from smoke_test_1 import SmokeTestSwagLabs
from smoke_test_1 import choice_browser

# Создания экземпляра класса для теста
test = SmokeTestSwagLabs(choice_browser())

# Непосредственно тестирование через метод класса
test.test1()
