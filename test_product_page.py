from selenium.webdriver.common.by import By
import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.compare_name_and_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, links[0])
    page.open()
    page.should_be_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, links[0])
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, links[0])
    page.open()
    page.should_be_add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_see_emty_basket_text()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():  
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/" 
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "BDIsdfV@$Y&#@"
        page = LoginPage(browser, self.login_link)
        page.open()
        page.should_be_login_url() 
        page.register_new_user(self.email, self.password)
        page.should_be_authorized_user()

    def  test_user_cant_see_success_message(self, browser):     
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
        page.open()
        page.should_be_add_product_in_basket()
        page.compare_name_and_price()



# @pytest.mark.login
# class TestLoginFromProductPage():
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title = "Best book created by robot")
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали 
#         self.product.delete()
        

#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста

#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста

    

    
    
    