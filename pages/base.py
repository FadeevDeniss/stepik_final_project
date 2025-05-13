from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def find_element(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.browser, timeout=timeout).until(
            ec.presence_of_element_located(locator),
            message=f'Element {locator} not found'
        )

    def find_elements(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.browser, timeout=timeout).until(
            ec.presence_of_all_elements_located(locator),
            message=f'Elements {locator} not found'
        )

    def open_page(self):
        self.browser.get(self.url)

