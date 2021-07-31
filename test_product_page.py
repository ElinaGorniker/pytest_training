from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()    
    page.msg_add_to_basket_presented()
    time.sleep(5)
    page.book_name_presented_in_add_msg()
    time.sleep(5)
    page.book_name_presented_in_add_msg()
    