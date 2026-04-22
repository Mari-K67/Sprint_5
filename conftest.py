import pytest
from selenium import webdriver
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def email():
    return f"test_user_{random.randint(100000, 999999)}@mail.ru"

@pytest.fixture
def invalid_email():
    return f"test_user_{random.randint(100000, 999999)}mairu"