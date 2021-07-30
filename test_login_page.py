from .pages.login_page import LoginPage

def test_login_url_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open() # открываем страницу
    page.should_be_login_url()

def test_login_form_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open() # открываем страницу
    page.should_be_login_form()
    
def test_register_form_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open() # открываем страницу
    page.should_be_register_form()