from .base import BasePage

from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    LOCATOR_LOGIN_FORM: tuple[str, str] = (By.CSS_SELECTOR, '#login_form')
    LOCATOR_REGISTRATION_FORM: tuple[str, str] = (By.CSS_SELECTOR, '#register_form')

    LOCATOR_REGISTRATION_FORM_EMAIL: tuple[str, str] = (By.CSS_SELECTOR, '#id_registration-email')
    LOCATOR_REGISTRATION_FORM_PASSWORD1: tuple[str, str] = (By.CSS_SELECTOR, '#id_registration-password1')
    LOCATOR_REGISTRATION_FORM_PASSWORD2: tuple[str, str] = (By.CSS_SELECTOR, '#id_registration-password2')
    LOCATOR_REGISTRATION_FORM_SUBMIT: tuple[str, str] = (By.CSS_SELECTOR, 'button[name="registration_submit')
    LOCATOR_REGISTRATION_SUCCESS: tuple[str, str] = (By.CSS_SELECTOR, '#messages div.alertinner')

    def register_user(self, email: str, password: str) -> bool:
        email_input = self.find_element(self.LOCATOR_REGISTRATION_FORM_EMAIL)
        password1_input = self.find_element(self.LOCATOR_REGISTRATION_FORM_PASSWORD1)
        password2_input = self.find_element(self.LOCATOR_REGISTRATION_FORM_PASSWORD2)
        submit_btn = self.find_element(self.LOCATOR_REGISTRATION_FORM_SUBMIT)

        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        submit_btn.click()

        return self.element_is_present(self.LOCATOR_REGISTRATION_SUCCESS)

    def should_be_login_url(self) -> bool:
        return 'login' in self.current_url

    def should_be_login_form(self) -> bool:
        return self.find_element(self.LOCATOR_LOGIN_FORM).is_displayed()

    def should_be_registration_form(self) -> bool:
        return self.find_element(self.LOCATOR_REGISTRATION_FORM).is_displayed()
