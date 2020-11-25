import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # пометим тест, как ожидаемо падающий с помощью xfail
    # Пока разработчики исправляют баг, мы хотим, чтобы результат прогона всех наших тестов был успешен,
    # но падающий тест помечался соответствующим образом, чтобы про него не забыть.

    # запускать с ключом -rx -v
    
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")
    
    # Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как XPASS (“unexpectedly passing” — неожиданно проходит)
    # После этого маркировку xfail для теста можно удалить.

    # ========= XPASS-тесты =========
    # Поменяем селектор в последнем тесте, чтобы тест начал проходить
    
    # запускать с ключом -rX -v
    
    # @pytest.mark.xfail(reason="fixing this bug right now")
    # def test_guest_should_see_search_button_on_the_main_page(self, browser):
    #     browser.get(link)
    #     browser.find_element_by_css_selector("input.btn.btn-default")