from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    MAIN_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group  .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR,"#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR,"[name = 'registration_submit']")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket") 
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    BASKET_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success")

class BasketPageLocators():
    CONTINUE_SHOPING = (By.CSS_SELECTOR, "#content_inner p a")
    VOUCHER_LINK = (By.CSS_SELECTOR, "#voucher_form_link")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    
        