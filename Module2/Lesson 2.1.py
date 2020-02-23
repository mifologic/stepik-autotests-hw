from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Капча для роботов
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/math.html")
x = driver.find_element(By.ID, "input_value").text
print(x)
y = calc(x)
field = driver.find_element(By.ID, "answer")
field.send_keys(y)
driver.find_element(By.ID, "robotCheckbox").click()
driver.find_element(By.ID, "robotsRule").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
