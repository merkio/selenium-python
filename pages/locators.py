from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_USERNAME = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USERNAME = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_BUTTON = (By.NAME, 'login_submit')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div.alert-success')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    BASKET_MINI = (By.CSS_SELECTOR, 'div.basket-mini')
    ALERTS = (By.CSS_SELECTOR, '#messages div.alertinner strong')


class BasketPageLocators:
    LIST_ITEMS = (By.CSS_SELECTOR, 'div.basket-items div.row')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
