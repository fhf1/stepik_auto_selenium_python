from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # находим первое и второе слагаемые (сразу в строковом формате)
    term1 = browser.find_element_by_id("num1").text
    term2 = browser.find_element_by_id("num2").text
    # посчитаем сумму слагаемых и приведем результат к строке
    sum_of_terms = int(term1) + int(term2)    
    # инициализируем новый объект, передав в него WebElement с тегом select
    select = Select(browser.find_element_by_class_name("custom-select"))
    # выберем из выпадающего списка значение равное полученной сумме
    select.select_by_value(str(sum_of_terms))
    # нажимаем submit
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
