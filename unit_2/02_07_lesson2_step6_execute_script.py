from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    # считываем значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    # используем атрибут .text для найденного элемента
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента.
    x = x_element.text
    # посчитаем матем.функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    
    field_for_calc_value = browser.find_element_by_id("answer")
    sel_chekbox_robot = browser.find_element_by_id("robotCheckbox")
    sel_radio_robot = browser.find_element_by_id("robotsRule")
    button = browser.find_element_by_tag_name("button")
    # скроллим страницу
    # browser.execute_script("window.scrollBy(0, 100);")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field_for_calc_value)
     
    field_for_calc_value.send_keys(y)    
    sel_chekbox_robot.click()    
    sel_radio_robot.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
