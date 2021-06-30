import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language_name', action='store', default=None,
                     help="Choose language: ru or en")


"""
Функция-пояснение что делать при выборе
того или иного языка
"""


@pytest.fixture(scope="function")
def language(request):
    language_name = request.config.getoption("language_name")
    if language_name == "es":
        language_name = "es"
    elif language_name == "en":
        language_name = "en-gb"
    link = f"http://selenium1py.pythonanywhere.com/{language_name}/catalogue/coders-at-work_207/"
    browser.get(link)


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
