from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login Form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register Form is not present'

    def register_new_user(self, email, password):
        register_username = self.browser.find_element(*LoginPageLocators.REGISTER_USERNAME)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_username.send_keys(email)
        register_password.send_keys(password)
        register_password_confirm.send_keys(password)
        register_button.click()
