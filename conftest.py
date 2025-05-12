import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='ru',
        help='Language code should contain two letters'
    )


@pytest.fixture(scope='session', autouse=True)
def language(request):
    return request.config.getoption('language')


@pytest.fixture
def browser(request, language):

    if len(language) > 2 or language.isnumeric():
        raise pytest.UsageError('--language option should contain two letters')

    browser = webdriver.Chrome()
    yield browser

    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def page_url(request, language):
    return f'https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
