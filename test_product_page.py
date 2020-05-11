from selenium.webdriver.remote.webdriver import WebDriver

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest
import time


@pytest.mark.guest_add_to_basket
class TestAddToBasketFromProductPage:

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                                   "/?promo=offer7", marks=pytest.mark.xfail),])
    def test_guest_can_add_product_to_basket(self, browser: WebDriver, link: str):
        page = ProductPage(browser, link)
        page.open()
        title, price = page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_in_basket(title)
        page.should_be_basket_cost_same_as_product(price)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items()
        basket_page.should_be_empty_basket_message()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: WebDriver):
        link = 'http://selenium1py.pythonanywhere.com'
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = '!O123456789'
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"
        page = ProductPage(browser, link)
        page.open()
        title, price = page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_in_basket(title)
        page.should_be_basket_cost_same_as_product(price)

    def test_user_cant_see_success_message(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.login
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser: WebDriver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
