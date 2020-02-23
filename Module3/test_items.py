import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_should_have_add_to_cart_button(browser):
    """ Проверяем, что на странице есть кнопка 'Добавить в корзину' на выбранном языке"""
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button, "Button not found"


