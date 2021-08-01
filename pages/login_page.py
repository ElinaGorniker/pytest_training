from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not presented in Url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
    
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        email_area =  self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_area.send_keys(email)
        password1_area = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password1_area.send_keys('qwerty67poiuy')
        password2_area = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password2_area.send_keys('qwerty67poiuy')
        confirm_button = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_BUTTON)
        confirm_button.click()
        
        