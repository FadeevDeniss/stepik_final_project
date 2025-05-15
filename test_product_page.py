import pytest

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
