# Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.
# Назначение фикстур может быть самым разным. 
# Одно из распространенных применений фикстур — это подготовка тестового окружения и очистка тестового окружения и данных после завершения теста.
# Но, вообще говоря, фикстуры можно использовать для самых разных целей: 
# для подключения к базе данных, с которой работают тесты, создания тестовых файлов или подготовки данных в текущем окружении с помощью API-методов. 
# Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами
# Можно создавать фикстуры для модулей, классов и отдельных функций. 

# Напишем фикстуру для инициализации браузера, который мы затем сможем использовать в наших тестах.
# После окончания тестов мы будем автоматически закрывать браузер с помощью команды browser.quit(), 
# чтобы в нашей системе не оказалось множество открытых окон браузера.
# Вынесем инициализацию и закрытие браузера в фикстуры, чтобы не писать этот код для каждого теста.

# Будем сразу объединять наши тесты в тест-сьюты, роль тест-сьюта будут играть классы, в которых мы будем хранить наши тесты.

# Рассмотрим два примера:
# создание экземпляра браузера и его закрытие только один раз для всех тестов первого тест-сьюта
# и создание браузера для каждого теста во втором тест-сьюте. Второй вариант - более оптимальный.

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():
    
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite #1..")
        self.browser = webdriver.Chrome()
    
    @classmethod
    def teardown_class(self):
        print("quit browser for test suite #1..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("start test login link 1")
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_quest_should_see_basket_link_on_the_main_page(self):
        print("start test basket link 1")
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

class TestMainPage2():

    def setup_method(self):
        print("start browser for test suite 2..")
        self.browser = webdriver.Chrome()
    
    def teardown_method(self):
        print("quit browser for testsuite 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("start test login link 2")
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")
    
    def test_quest_should_see_basket_link_on_the_main_page(self):
        print("start test basket link 2")
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")