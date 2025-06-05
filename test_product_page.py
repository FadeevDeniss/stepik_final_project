import random
import string
import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.open_page()
    product_page.add_to_cart()

    assert product_page.element_is_not_present(locator=ProductPage.LOCATOR_PRODUCT_ADDED_MESSAGE), \
        'Guest can see success message'


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, product_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.open_page()
    product_page.add_to_cart()

    assert product_page.element_is_disappeared(locator=ProductPage.LOCATOR_PRODUCT_ADDED_MESSAGE), \
        'Message is not disappeared after adding product to basket'


def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, url)
    product_page.open_page()

    assert product_page.should_be_login_link(), 'No login link is present on product page'


def test_guest_can_go_to_login_page_from_product_page(browser, product_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.open_page()
    product_page.open_login_page()

    login_page = LoginPage(browser, product_page.current_url)

    assert login_page.should_be_login_url(), \
        f"Can't go to login page from product page. Current url is {login_page.current_url}"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, product_page_url):
    product_page = ProductPage(browser, product_page_url)
    product_page.open_page()
    product_page.open_basket_page()

    basket_page = BasketPage(browser, product_page.current_url)

    assert basket_page.basket_is_empty(), 'Basket has items in it'
    assert basket_page.should_be_basket_empty_message(), 'There is no message of empty basket'


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, main_page_url):
        main_page = MainPage(browser, main_page_url)
        main_page.open_page()
        main_page.open_login_page()

        login_page = LoginPage(browser, main_page.current_url)

        assert login_page.should_be_login_url(), f"Can't go to login page, current url is {login_page.current_url}"
        assert login_page.register_user(self.username, self.password(length=9)), 'User registration failed'
        assert login_page.should_be_authorized_user(), 'User not authorized'

    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        product_page = ProductPage(browser, url)
        product_page.open_page()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()

        assert product_page.should_be_message_with_added_product(), 'No success message of added product'
        assert product_page.should_be_message_cart_total_price_change(), 'No message of cart total price'

        assert product_page.product_added_name_should_be_equal_to_product_name(), \
            'Added product name and product name from description are not equal'
        assert product_page.product_added_price_should_be_equal_to_product_price(), \
            'Added product price and product price from description are not equal'

    def test_user_cant_see_success_message(self, browser, product_page_url):
        product_page = ProductPage(browser, product_page_url)
        product_page.open_page()

        assert product_page.element_is_not_present(locator=ProductPage.LOCATOR_PRODUCT_ADDED_MESSAGE), \
            'Guest can see success message without adding a product to basket'

    @property
    def username(self):
        return f'user{time.time():.0f}@fakemail.com'

    @staticmethod
    def password(length: int = 12):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
