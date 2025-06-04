from .base import BasePage

from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    LOCATOR_LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOCATOR_REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

    def should_be_login_url(self) -> bool:
        return 'login' in self.current_url

    def should_be_login_form(self):
        return self.find_element(self.LOCATOR_LOGIN_FORM).is_displayed()

    def should_be_register_form(self):
        return self.find_element(self.LOCATOR_REGISTRATION_FORM).is_displayed()
