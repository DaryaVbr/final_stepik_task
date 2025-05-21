from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        # self.code_is_gotten()
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        text_add = self.browser.find_element(*ProductPageLocators.TEXT_ADD)
        text_message = text_add.text
        book_message = name_book.text
        assert book_message == text_message, "текст отличается, либо отсутствует"

    def should_be_cost_of_book_in_cart(self):
        cost_in_cart = self.browser.find_element(*ProductPageLocators.COST_IN_CART)
        cost_of_book = self.browser.find_element(*ProductPageLocators.COST_OF_BOOK)
        cost_cart_text = cost_in_cart.text
        cost_book_text = cost_of_book.text
        assert cost_book_text == cost_cart_text, "цена не соответствует или не найдена"

    def code_is_gotten(self):
        return self.solve_quiz_and_get_code(), "кода нет.что-то пошло не так"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def is_not_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success object is presented, but should not be"
