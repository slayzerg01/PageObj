from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "В корзине присутствуют товары"
    
    def should_be_see_emty_basket_text(self):
        self.browser.find_element(*BasketPageLocators.CONTINUE_SHOPING).click()
        assert not "basket" in self.browser.current_url, "Отсутствует текст о том что корзина пуста"