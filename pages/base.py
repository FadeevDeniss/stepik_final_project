import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoAlertPresentException


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def current_url(self) -> str:
        return self.browser.current_url

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

    def element_is_present(self, locator: tuple[str, str], timeout: int = 10) -> bool:
        try:
            self.find_element(locator, timeout)
        except TimeoutException:
            return False
        return True

    @staticmethod
    def text_of_element(element: WebElement):
        return element.text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def open_page(self):
        self.browser.get(self.url)
