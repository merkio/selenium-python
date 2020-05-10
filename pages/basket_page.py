from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_message(self):
        assert 'Your basket is empty' in \
               self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text.strip()

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_ITEMS), "Items list is not empty"
