from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open() # открываем страницу
    page.go_to_login_page() # переходим на страницу логина
def test_guest_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
 
def test_login_url_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = MainPage(browser, link)
    page.open() # открываем страницу
    page.should_be_login_url()

def test_login_form_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = MainPage(browser, link)
    page.open() # открываем страницу
    page.should_be_login_form()
    
def test_register_form_is_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = MainPage(browser, link)
    page.open() # открываем страницу
    page.should_be_register_form()
    