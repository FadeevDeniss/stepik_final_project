import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser, main_page_url):
        main_page = MainPage(browser, main_page_url)
        main_page.open_page()
        main_page.open_login_page()

        login_page = LoginPage(browser, browser.current_url)

        assert login_page.should_be_login_url(), 'No element \'login\'is presented'
        assert login_page.should_be_login_form(), 'No element \'login form\'is presented'
        assert login_page.should_be_registration_form(), 'No element \'registration form\'is presented'

    def test_guest_should_see_login_link(self, browser, main_page_url):
        main_page = MainPage(browser, main_page_url)
        main_page.open_page()

        assert main_page.should_be_login_link(), 'Login link not present.'


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, main_page_url):
    main_page = MainPage(browser, main_page_url)
    main_page.open_page()
    main_page.open_basket_page()

    basket_page = BasketPage(browser, main_page.current_url)

    assert basket_page.basket_is_empty(), 'Basket has items in it'
    assert basket_page.should_be_basket_empty_message(), 'There is no message of empty basket'
