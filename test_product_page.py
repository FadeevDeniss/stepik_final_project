import pytest

from pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('url', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, url):
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, page_url):
    product_page = ProductPage(browser, page_url)
    product_page.open_page()
    product_page.add_to_cart()

    assert product_page.element_is_not_present(locator=ProductPage.LOCATOR_PRODUCT_ADDED_MESSAGE), \
        'Guest can see success message'


def test_guest_cant_see_success_message(browser, page_url):
    product_page = ProductPage(browser, page_url)
    product_page.open_page()

    assert product_page.element_is_not_present(locator=ProductPage.LOCATOR_PRODUCT_ADDED_MESSAGE), \
        'Guest can see success message without adding a product to basket'


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, page_url):
    product_page = ProductPage(browser, page_url)
    product_page.open_page()
    product_page.add_to_cart()

    assert product_page.element_is_disappeared(locator=ProductPage.LOCATOR_PRODUCT_ADDED_MESSAGE), \
        'Message is not disappeared after adding product to basket'


def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, url)
    product_page.open_page()

    assert product_page.should_be_login_link(), 'No login link is present on product page'


def test_guest_can_go_to_login_page_from_product_page(browser, page_url):
    product_page = ProductPage(browser, page_url)
    product_page.open_page()
    product_page.open_login_page()

    login_page = LoginPage(browser, product_page.current_url)

    assert login_page.should_be_login_url(), \
        f"Can't go to login page from product page. Current url is {login_page.current_url}"
