from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_empty_text(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_MESSAGE), "Empty message is absent or there are books"

    def should_not_be_goods(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_GOODS), "There are basket goods, but they shouldn't"

