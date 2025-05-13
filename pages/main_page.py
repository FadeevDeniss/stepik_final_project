from .base import BasePage

from selenium.webdriver.common.by import By


class MainPage(BasePage):

    LOCATOR_LOGIN_LINK: tuple[str, str] = (By.CSS_SELECTOR, "#login_link")

    def open_login_page(self):
        login_link = self.find_element(MainPage.LOCATOR_LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self) -> bool:
        return self.element_is_present(self.LOCATOR_LOGIN_LINK)
