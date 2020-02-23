import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("link", ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_parametrization_feedback(driver, link):

    answer = math.log(int(time.time()))

    driver.get(link)
    textarea = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea")))
    textarea.send_keys(str(answer))
    driver.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    text = message.text
    assert text == "Correct!"
