from pages.base import BasePage

from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    LOCATOR_BASKET_PRODUCTS: tuple[str, str] = (By.CSS_SELECTOR, '#basket_formset')
    LOCATOR_BASKET_EMPTY: tuple[str, str] = (By.CSS_SELECTOR, '#content_inner > p')

    def basket_is_empty(self) -> bool:
        return self.element_is_not_present(self.LOCATOR_BASKET_PRODUCTS)

    def should_be_basket_empty_message(self) -> bool:
        return 'корзина пуста' in self.find_element(self.LOCATOR_BASKET_EMPTY).text
