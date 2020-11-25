import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# В параметрах можно задать список товаров (как части URL), для примера взят один товар:
@pytest.mark.parametrize("product", [
    'coders-at-work_207'
    ])
def test_guest_should_see_add_to_basket_button_on_product_page(browser, product):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/{product}/"  
    browser.get(link)
    # time.sleep(5)
    
    # Проверим, что страница товара на сайте содержит кнопку добавления в корзину
    # и кнопка не только отображается, но также имеет высоту и ширину больше нуля:
    button_add_to_basket = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
        )
    assert button_add_to_basket.is_displayed() == True, "Страница товара не содержит кнопку добавления в корзину"
