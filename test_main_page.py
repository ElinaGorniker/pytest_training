from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open() # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  
    login_page.should_be_login_page()
@pytest.mark.skip    
def test_guest_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_go_to_basket_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()   
    page.go_to_basket()
    page.should_be_empty_msg()
    page.basket_should_be_empty()

  

   