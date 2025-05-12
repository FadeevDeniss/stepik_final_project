from .base import BasePage

from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def open_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
