from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять в течение 12 секунд, пока цена дома уменьшится до $100.
    # Здесь надо использовать поиск элементов с помощью класса By.
    # В объекте WebDriverWait используется функция until, в которую передается 
    # правило ожидания, элемент, а также значение, по которому мы будем искать элемент.
    price_home = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # text_to_be_present_in_element вернет элемент, когда цена достигнет 100$, или вернет False в ином случае.

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
        )
    # element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.

    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    btn_submit = browser.find_element_by_id("solve")
    btn_submit.click()

finally:
    time.sleep(8)
    browser.quit()
