import pytest
from selenium.webdriver.common.by import By
from automation import setup_driver, fill_station_field, select_date, search_tickets

@pytest.fixture(scope="module")
def driver():
    drv = setup_driver()
    yield drv
    drv.quit()

def test_fill_search(driver):
    fill_station_field(driver, "origination-flexdatalist", "GAMBIR")
    fill_station_field(driver, "destination-flexdatalist", "YOGYAKARTA")
    assert select_date(driver) == True
    result = search_tickets(driver)

    is_card_exist = driver.find_element(By.CLASS_NAME, 'month-wrapper').is_displayed()
    assert is_card_exist == True