from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6>H1")
    TEXT_ADD = (By.CSS_SELECTOR, "#messages > div.alert:nth-child(1)>div.alertinner strong")
    COST_IN_CART = (By.CSS_SELECTOR, "#messages > div.alert:nth-child(3)>div.alertinner>p strong")
    COST_OF_BOOK = (By.CSS_SELECTOR, "div.col-sm-6>p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert:nth-child(1)>div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a.btn.btn-default")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_GOODS = (By.CSS_SELECTOR, "div.basket-items")

