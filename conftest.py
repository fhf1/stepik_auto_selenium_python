import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# добавляем обработчик опции в функции pytest_addoption
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                    help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                    help="Choose language: ru, en, ...(etc.)")    

# напишем фикстуру, которая будет обрабатывать переданные в опции данные
@pytest.fixture(scope="function")
def browser(request):
    # Для запроса значения параметра мы можем вызвать команду:
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")    
    if browser_name == "chrome":        
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":        
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# Сколько бы файлов с тестами мы ни создали, у тестов будет доступ к фикстуре browser.
# Фикстура передается в тестовый метод в качестве аргумента.
# Таким образом можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.
