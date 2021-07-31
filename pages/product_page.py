from .base_page import BasePage
from .locators import ProductPageLocators
import time

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
        
