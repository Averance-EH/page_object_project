import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose any language available by using correct parameter")


@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption("language")
    # browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print('\nstart browser..')
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

    