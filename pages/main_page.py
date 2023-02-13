from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs) #The super() function is used to give access to methods and properties of a parent or sibling class  
                                                        #Constructor, called every time an object is created from a class, 
                                                        #*kwargs allows us to pass a variable number of keyword arguments to a Python function
                                                        #*args allows us to pass a variable number of non-keyword arguments to a Python function.
