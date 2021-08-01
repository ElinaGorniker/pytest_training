from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.skip
def test_login_url_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open() # открываем страницу
    page.should_be_login_url()
@pytest.mark.skip
def test_login_form_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open() # открываем страницу
    page.should_be_login_form()
@pytest.mark.skip
def test_register_form_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open() # открываем страницу
    page.should_be_register_form()
    
def test_guest_register(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open() 
    page.register_new_user()
    time.sleep(5)
    page.should_be_authorized_user()

