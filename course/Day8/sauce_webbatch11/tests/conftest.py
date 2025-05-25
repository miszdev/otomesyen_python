from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Firefox()

    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get('https://saucedemo.com')
    
    yield driver   
    
    driver.close()