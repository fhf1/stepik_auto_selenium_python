from selenium import webdriver

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_for_except = browser.find_element_by_id("button")
finally:
    browser.quit()
    