from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Not login url"
    
    def register_new_user(self, email, password):
        register_mail = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL)
        register_pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        register_pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_mail.send_keys(email)
        register_pass1.send_keys(password)
        register_pass2.send_keys(password)
        register_button.click()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Not login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Not register form"