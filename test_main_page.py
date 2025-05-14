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
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)

    # Open main page and check login link
    page.open_page()
    assert page.should_be_login_link(), 'Login link not present.'
