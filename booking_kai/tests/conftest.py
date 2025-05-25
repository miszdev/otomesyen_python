# tests/conftest.py
import pytest
from selenium import webdriver
from pages.search_page import KaiSearchPage


@pytest.fixture(scope="module")
def driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    drv = webdriver.Chrome(options=option)
    drv.maximize_window()
    drv.get("https://booking.kai.id/ ")
    yield drv
    drv.quit()


@pytest.fixture
def kai_search_page(driver):
    return KaiSearchPage(driver)