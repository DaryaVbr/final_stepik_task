from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "url адрес не для авторизации"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "формы авторизации не найдено"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "формы регистрации не найдено"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        repeat_password = self.browser.find_element(*RegisterPageLocators.REPEAT_PASSWORD)
        repeat_password.send_keys(password)
        register_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()