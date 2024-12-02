from smoke_test_1 import Smoke_Test_Swag_labs
from smoke_test_1 import choice_browser

# Создания экземпляра класса для теста
test = Smoke_Test_Swag_labs(choice_browser())

# Непосредственно тестирование через метод класса
test.test1()
