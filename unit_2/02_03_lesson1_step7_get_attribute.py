from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # находим элемент-картинку, который является изображением сундука с сокровищами.
    sunduk = browser.find_element_by_id("treasure")
    # берем у этого элемента значение атрибута valuex, которое является значением x для задачи
    x = sunduk.get_attribute("valuex")
    # посчитаем матем.функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
    # встаем в поле для ввода вычисленого значения y
    field_for_calc_value = browser.find_element_by_id("answer")
    # вводим значение y
    field_for_calc_value.send_keys(y)

    sel_checkbox_robot = browser.find_element_by_id("robotCheckbox")
    sel_checkbox_robot.click()
    sel_radio_robot = browser.find_element_by_id("robotsRule")
    sel_radio_robot.click()
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
finally:
    time.sleep(15)
    browser.quit()
    