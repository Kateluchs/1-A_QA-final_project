import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Need choose language')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Need choose browser: chrome or firefox')  # add default browser


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        options = Options()
        print('\nStart CHROME browser for test..')
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        print("\nStart FIREFOX browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--Choose browser: chrome or firefox")

    yield browser
    print("\nQuit browser..")