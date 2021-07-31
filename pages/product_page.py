from .base_page import BasePage
from .locators import ProductPageLocators
import time
import pytest

class ProductPage(BasePage):
    def add_to_basket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        busket_button.click()
        self.solve_quiz_and_get_code()
                
    def msg_add_to_basket_presented(self):
        msg = self.browser.find_element(*ProductPageLocators.MSG_ADD_TO_BASKET).text
        assert "has been added to your basket" in msg, "Massage is not presented or incorrect"
        
    def book_name_presented_in_add_msg(self):
        book_in_shop_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MSG).text
        book_in_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_SHOP).text
        assert book_in_shop_name == book_in_basket_name, "Book name is not equal"    
    def price_is_equal(self):
        price_in_shop = self.browser.find_element(*ProductPageLocators.PRICE_IN_SHOP).text
        price_in_msg = self.browser.find_element(*ProductPageLocators.PRICE_IN_MSG).text
        assert price_in_shop == price_in_msg, "Price is not equal" 
    
    def promo_is_possible(self):
        promo_msg = self.browser.find_element(*ProductPageLocators.PROMO_MSG).text
        #assert promo_msg == "Deferred benefit offer", "Promo is not possible" 
        #assert promo_msg == '" Ваша корзина удовлетворяет условиям предложения "', "Promo is not possible"
        assert 'корзина удовлетворяет' in promo_msg, "Promo is not possible"