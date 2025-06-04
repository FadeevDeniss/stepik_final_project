import math

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoAlertPresentException


class BasePage:
    LOCATOR_LOGIN_LINK: tuple[str, str] = (By.CSS_SELECTOR, "#login_link")
    LOCATOR_LOGIN_LINK_INVALID: tuple[str, str] = (By.CSS_SELECTOR, "#login_link_inc")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    @property
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

    def element_is_present(self, locator: tuple[str, str], timeout: int = 10):
        try:
            self.find_element(locator, timeout)
        except TimeoutException:
            return False
        return True

    def element_is_not_present(self, locator: tuple[str, str], timeout: int = 10) -> bool:
        try:
            self.find_element(locator, timeout)
        except TimeoutException:
            return True
        return False

    def element_is_disappeared(self, locator: tuple[str, str], timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.browser, timeout=timeout).until_not(
                ec.presence_of_element_located(locator)
            )
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

    def open_login_page(self):
        link = self.find_element(self.LOCATOR_LOGIN_LINK)
        link.click()

    def should_be_login_link(self) -> bool:
        return self.element_is_present(self.LOCATOR_LOGIN_LINK)
