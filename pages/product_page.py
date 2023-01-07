from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_product_in_basket(self):
        self.product_name = None
        self.product_price = None
        self.should_be_get_product_name()
        self.should_be_get_product_price()
        self.should_be_see_basket_button()
        self.click_basket_button()
        self.solve_quiz_and_get_code()
        self.should_be_compare_product_names()
        self.should_be_compare_prices()

    def should_be_see_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Not Basket Button"

    def click_basket_button(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        
    def should_be_get_product_name(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_get_product_price(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_compare_product_names(self):
        assert self.product_name == self.browser.find_element(*ProductPageLocators.BASKET_NAME).text, "Наименование \
        продукта в корзине не совпадает"

    def should_be_compare_prices(self):
        assert self.product_price == self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text, "Стоимость \
        корзины не совпадает с ценой товара"

    
