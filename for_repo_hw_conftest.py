import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем обработчик, который считывает из командной строки параметр language:
def pytest_addoption(parser):
    parser.addoption('--language', \
                    action='store', \
                    default=None, \
                    help="Choose language: ru, en, ... (etc.)")

@pytest.fixture(scope='function')
def browser(request):
    # Реализация логики запуска браузера с указанным языком пользователя:
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    