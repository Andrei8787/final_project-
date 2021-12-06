from pages.test_product_page import ProductPage
import time
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page.open()                         # открываем страницу.
    page.add_to_basket()                # кликнуть на кнопку Добавить в корзину.
    page.solve_quiz_and_get_code()      # выполнение метода для получения проверочного кода.
    page.should_be_product_add_to_basket()        # Проверка на добавление товара в корзину.
