import math

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoAlertPresentException


class BasePage:

    LOCATOR_LOGIN_LINK: tuple[str, str] = (By.CSS_SELECTOR, "#login_link")
    LOCATOR_BASKET_LINK: tuple[str, str] = (By.CSS_SELECTOR, 'a[href="/ru/basket/"]')
    LOCATOR_LOGIN_LINK_INVALID: tuple[str, str] = (By.CSS_SELECTOR, "#login_link_inc")
    LOCATOR_USER_ICON: tuple[str, str] = (By.CSS_SELECTOR, ".icon-user")

    def __init__(self, browser: Chrome, url: str):
        self.browser = browser
        self.url = url

    @property
    def current_url(self) -> str:
        return self.browser.current_url

    def find_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        return WebDriverWait(self.browser, timeout=timeout).until(
            ec.presence_of_element_located(locator),
            message=f'Element {locator} not found'
        )

    def find_elements(self, locator: tuple[str, str], timeout: int = 10) -> list[WebElement]:
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

    def open_page(self) -> None:
        self.browser.get(self.url)

    def open_login_page(self) -> None:
        link = self.find_element(self.LOCATOR_LOGIN_LINK)
        link.click()

    def open_basket_page(self) -> None:
        link = self.find_element(self.LOCATOR_BASKET_LINK)
        link.click()

    def should_be_login_link(self) -> bool:
        return self.element_is_present(self.LOCATOR_LOGIN_LINK)

    def should_be_authorized_user(self):
        return self.element_is_present(self.LOCATOR_USER_ICON)
