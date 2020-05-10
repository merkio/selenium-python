from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import re


class ProductPage(BasePage):

    def add_product_to_basket(self):
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        return title, price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def should_be_product_in_basket(self, title):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERTS)
        alerts_texts = list(map(lambda e: e.text, alerts))
        assert title in alerts_texts, f"Product {title} is not in the basket"

    def should_be_basket_cost_same_as_product(self, price):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERTS)
        alerts_texts = list(map(lambda e: e.text, alerts))
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        basket_total = re.search(r'.\d+\.\d+', basket_total).group().strip()
        assert price in alerts_texts, f"Product price in alert is not correct"
        assert price == basket_total, f"Product price in mini basket is not correct"
