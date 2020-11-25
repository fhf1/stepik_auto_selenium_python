from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")
# заставляем браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
# Мы дополнительно передали в метод scrollIntoView аргумент true, чтобы элемент после скролла оказался в области видимости.
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскроллить страницу.
button.click()
assert True

# Еще примеры скриптов:

# Эта команда проскроллит страницу на 100 пикселей вниз:
# browser.execute_script("window.scrollBy(0, 100);")

# browser.execute_script("alert('Robots at work');")

# browser.execute_script("document.title='Script executing';")

# сразу несколько инструкций, перечислим их через точку с запятой
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
