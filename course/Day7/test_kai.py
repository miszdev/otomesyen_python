import pytest
from kai import setup_driver, fill_station_field, select_date, search_tickets
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    drv = setup_driver()
    yield drv
    drv.quit()

# def test_before_text(driver):
#     """Pastikan halaman awal berisi teks 'Pemesanan Tiket Kereta Api'"""
#     header = driver.find_element(By.CSS_SELECTOR, "h2.media-heading")
#     assert "Pemesanan Tiket Kereta Api" in header.text

def test_fill_and_search(driver):
    """Test alur pencarian tiket dan validasi teks setelah pencarian"""
    fill_station_field(driver, "origination-flexdatalist", "GAMBIR")
    fill_station_field(driver, "destination-flexdatalist", "YOGYAKARTA")
    assert select_date(driver) == True
    result = search_tickets(driver)
    # assert "tidak ada" not in result.lower()  # bisa juga test isi lainnya

    isCardExist = driver.find_element(By.CLASS_NAME, 'month-wrapper').is_displayed()
    assert isCardExist == True

# def test_after_text(driver):
#     """Validasi teks GAMBIR → YOGYAKARTA muncul setelah pencarian"""
#     route = driver.find_element(By.CSS_SELECTOR, "div.media-heading h4")
#     assert "GAMBIR" in route.text and "YOGYAKARTA" in route.text

