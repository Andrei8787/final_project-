from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket") # Кнопка Добавить в корзину.
    NAME_ADD_BASKET = (By.CSS_SELECTOR, ".alertinner strong")  # Добавленная книга в корзине.
    PRICE_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alertinner p strong") # Сообщения с ценой о добавлении в корзину.
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color") # Цена добавляемого товара.