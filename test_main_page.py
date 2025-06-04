from pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)

    # Open main page, then go login page
    main_page.open_page()
    main_page.open_login_page()

    # Check that we are on a login page
    login_page = LoginPage(browser, browser.current_url)

    assert login_page.should_be_login_url(), 'No element \'login\'is presented'
    assert login_page.should_be_login_form(), 'No element \'login form\'is presented'
    assert login_page.should_be_register_form(), 'No element \'registration form\'is presented'


def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)

    # Open main page and check login link
    page.open_page()
    assert page.should_be_login_link(), 'Login link not present.'


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, url)
    main_page.open_page()
    main_page.open_basket_page()

    basket_page = BasketPage(browser, main_page.current_url)

    assert basket_page.basket_is_empty(), 'Basket has items in it'
    assert basket_page.should_be_basket_empty_message(), 'There is no message of empty basket'
