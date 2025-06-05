from selenium.webdriver.common.by import By

from .base import BasePage


class ProductPage(BasePage):

    LOCATOR_PRODUCT_NAME: tuple[str, str] = (By.CSS_SELECTOR, '#content_inner .row > .product_main > h1')
    LOCATOR_PRODUCT_PRICE: tuple[str, str] = (By.CSS_SELECTOR, '#content_inner .row > .product_main > .price_color')
    LOCATOR_ADD_TO_CART_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, '#add_to_basket_form > [type="submit"]')
    LOCATOR_PRODUCT_ADDED_MESSAGE: tuple[str, str] = (By.CSS_SELECTOR, '#messages > :first-child')
    LOCATOR_CART_TOTAL_PRICE_MESSAGE: tuple[str, str] = (By.CSS_SELECTOR, '#messages > :last-child')
    LOCATOR_PRODUCT_ADDED_MESSAGE_TEXT: tuple[str, str] = (By.CSS_SELECTOR, '#messages > :first-child strong')
    LOCATOR_CART_TOTAL_PRICE_MESSAGE_TEXT: tuple[str, str] = (By.CSS_SELECTOR, '#messages > :last-child strong')

    def add_to_cart(self) -> None:
        cart_btn = self.find_element(locator=self.LOCATOR_ADD_TO_CART_BUTTON)
        cart_btn.click()

    def product_name(self) -> str | None:
        return self.find_element(self.LOCATOR_PRODUCT_NAME).text

    def product_price(self) -> str | None:
        return self.find_element(self.LOCATOR_PRODUCT_PRICE).text

    def product_added_name_should_be_equal_to_product_name(self) -> bool:
        element = self.find_element(self.LOCATOR_PRODUCT_ADDED_MESSAGE_TEXT)
        return self.product_name() == element.text

    def product_added_price_should_be_equal_to_product_price(self) -> bool:
        element = self.find_element(self.LOCATOR_CART_TOTAL_PRICE_MESSAGE_TEXT)
        return self.product_price() == element.text

    def should_be_message_with_added_product(self) -> bool:
        return self.element_is_present(self.LOCATOR_PRODUCT_ADDED_MESSAGE)

    def should_be_message_cart_total_price_change(self) -> bool:
        return self.element_is_present(self.LOCATOR_CART_TOTAL_PRICE_MESSAGE)