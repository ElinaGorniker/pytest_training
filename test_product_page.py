from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()    
@pytest.mark.skip    
def test_msg_add_to_basket_presented(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()    
    page.msg_add_to_basket_presented()

@pytest.mark.skip
def test_book_name_in_msg_is_equal(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()    
    page.book_name_presented_in_add_msg()

@pytest.mark.skip
def test_price_in_msg_is_equal(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()    
    page.price_is_equal()  

@pytest.mark.skip
@pytest.mark.parametrize('link',['offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6', pytest.param("offer7", marks=pytest.mark.xfail), 'offer8', 'offer9'])
def test_guest_can_add_product_to_basket(browser, link):
    promo_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}'
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, promo_link)
    page.open()
    page.add_to_basket()
    #time.sleep(60)
    page.promo_is_possible()
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()    
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()    
    page.should_dissapeared_success_message()

    