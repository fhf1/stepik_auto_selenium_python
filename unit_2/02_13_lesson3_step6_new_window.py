from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    magic_button = browser.find_element_by_xpath("//button[@type='submit']")
    magic_button.click()
    # задаем имя новой вкладке, получив ее через метод window_handless:
    new_window = browser.window_handles[1]
    # переходим на новую вкладку
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()
finally:
    time.sleep(7)
    browser.quit()