import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# =======================
# FUNGSI UTAMA OTOMASI KAI
# =======================

def setup_driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://booking.kai.id/')
    return driver

def fill_station_field(driver, field_id, value):
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, field_id)))
    field.clear()
    field.send_keys(value)
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "flexdatalist-results"))
    )
    field.send_keys(Keys.DOWN, Keys.ENTER)

def select_date(driver):
    date_picker = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "departure_dateh")))
    date_picker.click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'ui-datepicker-div')))
    holiday = driver.find_elements(By.XPATH, '//td[@class=" holiday"]')
    if holiday:
        holiday[0].click()
        return True
    available = driver.find_elements(By.XPATH, 
        '//td[@data-handler="selectDay" and not(contains(@class, "ui-datepicker-unselectable"))]')
    if available:
        available[0].click()
        return True
    return False

def search_tickets(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "schedule-list")))
        return "Daftar tiket berhasil ditampilkan"
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loading")))
        if driver.find_elements(By.XPATH, "//div[contains(@class, 'alert-danger')]"):
            return "Tidak ada tiket tersedia"
        elif driver.find_elements(By.CLASS_NAME, "empty-schedule"):
            return "Tidak ada jadwal tersedia"
        else:
            return "Hasil pencarian selesai dimuat"

# =======================
# TEST MENGGUNAKAN PYTEST
# =======================

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

    isCardExist = driver.find_element(By.CLASS_NAME, 'month-wrapper').is_displayed()
    assert isCardExist == True


# ===========================
# OPSIONAL: JALANKAN LANGSUNG
# ===========================
if __name__ == "__main__":
    print("Jalankan dengan pytest: `pytest tugas5.py`")