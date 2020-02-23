import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    print("\ncreate driver for test")
    driver = webdriver.Chrome()
    yield driver
    print("\nclose browser after test")
    driver.quit()
