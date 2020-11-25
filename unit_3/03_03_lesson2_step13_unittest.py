import unittest
from selenium import webdriver
import time

class TestWelcomeText(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        req_input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        req_input1.send_keys("Vitaly")
        req_input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        req_input2.send_keys("Vertyakov")
        req_input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        req_input3.send_keys("vitaverty@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The expected text does not match the text on the page")
        
    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        req_input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        req_input1.send_keys("Vitaly")
        req_input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        req_input2.send_keys("Vertyakov")
        req_input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        req_input3.send_keys("vitaverty@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The expected text does not match the text on the page")

if __name__ == "__main__":
    unittest.main()
