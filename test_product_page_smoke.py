from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(1)
    page.promo_is_possible()
    time.sleep(1)
    
