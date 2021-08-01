from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_CONFIRM_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    BOOK_NAME_IN_MSG = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_NAME_IN_SHOP = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    MSG_ADD_TO_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    PRICE_IN_SHOP = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRICE_IN_MSG = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    #PROMO_MSG = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div > strong')
    PROMO_MSG = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a')
    
class BasketPageLocators():
    BASKET_LINK_IN_HEADER = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_MSG_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    GOOD_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div")
    