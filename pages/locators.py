from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    BOOK_NAME_IN_MSG = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_NAME_IN_SHOP = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    MSG_ADD_TO_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div')