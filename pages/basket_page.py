from .base_page import BasePage
from .locators import BasketPageLocators
import time
import pytest

class BasketPage(BasePage):
    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK_IN_HEADER)
        basket_link.click()
        
    def should_be_empty_msg(self):
        empty_msg = self.browser.find_element(*BasketPageLocators.BASKET_MSG_EMPTY).text
        assert "Your basket is empty" or "Ваша корзина пуста" in empty_msg, "Message 'Your basket is empty.' is not presented"
    
    def basket_should_be_empty(self):
       assert self.is_not_element_present(*BasketPageLocators.GOOD_IN_BASKET), "Basket is not empty"
    