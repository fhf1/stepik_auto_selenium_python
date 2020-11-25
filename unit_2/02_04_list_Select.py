from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = ""

browser = webdriver.Chrome()
browser.get(link)


browser.find_element_by_tag("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()
# либо так:
# browser.find_element_by_css_selector("[value='1']").click()

# более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver:
# инициализируем новый объект, передав в него WebElement с тегом select
select = Select(browser.find_element_by_tag_name("select"))
# ищем элемент с текстом "Python"
select.select_by_value("1")

# Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index)
# Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python")
# Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля.
# Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1), 
# так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".