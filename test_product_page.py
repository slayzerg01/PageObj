from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_in_basket()
    #page.solve_quiz_and_get_code()
    time.sleep(70)
    
    
    