from pages.locators import ProductPageLocators
from .base_page import BasePage
class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON) # Поиск кнопки Добавить в корзину.
        basket.click() # Нажать на кнопку.

    def should_be_product_add_to_basket(self):
        self.should_be_add_basket()
        self.should_be_correct_name()
        self.should_be_price()
        self.should_be_correct_price()

    def should_be_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "There is no message about adding an item to the cart" # Сообщение о добавлении в корзину.

    def should_be_correct_name(self):
        text_add_name = self.browser.find_element(*ProductPageLocators.NAME_ADD_BASKET).text # Наименование добавленного товара в корзину.
        text_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text # Наименование товара
        assert text_add_name == text_product, "Added the wrong product"

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_ADDED_TO_BASKET), "There is no message with the price of adding an item to the cart" # Проверка на появлении сообщения с ценой.

    def should_be_correct_price(self):          # Проверка на соотвесвтие цены товара.
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        add_price = self.browser.find_element(*ProductPageLocators.PRICE_ADDED_TO_BASKET).text
        assert add_price == price, "The price in the cart does not match the price of the item "

    def should_not_be_success_message(self): # Проверка на появление элемента в течение определённого времени.
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_appear(self): # Проверка на пропадание элемента.
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message does not disappear although it should"
    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

