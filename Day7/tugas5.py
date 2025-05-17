import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

def setup_driver():
    """Inisialisasi dan konfigurasi driver Chrome"""
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://booking.kai.id/')
    return driver

def fill_station_field(driver, field_id, value):
    """Mengisi field stasiun dan memilih dari dropdown"""
    field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, field_id)))
    field.clear()
    field.send_keys(value)
    
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "flexdatalist-results"))
    )
    
    field.send_keys(Keys.DOWN, Keys.ENTER)
    return True

def select_date(driver):
    """Memilih tanggal keberangkatan dari kalender"""
    date_picker = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "departure_dateh")))
    date_picker.click()
    
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'ui-datepicker-div')))
    
    # Coba pilih hari libur jika ada
    holiday = driver.find_elements(By.XPATH, '//td[@class=" holiday"]')
    if holiday:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//td[@class=" holiday"][1]')))
        holiday[0].click()
        return True
    
    # Jika tidak ada hari libur, pilih tanggal yang tersedia
    available_dates = driver.find_elements(By.XPATH, 
        '//td[@data-handler="selectDay" and not(contains(@class, "ui-datepicker-unselectable"))]')
    if available_dates:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, 
            '//td[@data-handler="selectDay" and not(contains(@class, "ui-datepicker-unselectable"))][1]')))
        available_dates[0].click()
        return True
    
    return False

def search_tickets(driver):
    """Mencari tiket dengan mengklik tombol pencarian"""
    submit_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit")))
    submit_button.click()
    
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "schedule-list")))
        return "Daftar tiket berhasil ditampilkan"
    except TimeoutException:
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loading")))
        
        if len(driver.find_elements(By.XPATH, "//div[contains(@class, 'alert-danger')]")) > 0:
            return "Tidak ada tiket tersedia"
        elif len(driver.find_elements(By.CLASS_NAME, "empty-schedule")) > 0:
            return "Tidak ada jadwal tersedia"
        else:
            return "Hasil pencarian selesai dimuat"

def book_kai_ticket(origin="JAKARTA", destination="YOGYAKARTA"):
    """Fungsi utama untuk memesan tiket KAI"""
    driver = setup_driver()
    
    try:
        fill_station_field(driver, "origination-flexdatalist", origin)
        fill_station_field(driver, "destination-flexdatalist", destination)
        date_selected = select_date(driver)
        
        if date_selected:
            result = search_tickets(driver)
            return result
        else:
            return "Gagal memilih tanggal"
    except Exception as e:
        return f"Error: {str(e)}"

# Test cases
test_data = [
    ("JAKARTA", "YOGYAKARTA"),
    ("BANDUNG", "SURABAYA"),
    ("PASARSENEN", "GANDRUNGMANGU")
]

@pytest.mark.parametrize('origin, destination', test_data)
def test_booking(origin, destination):
    result = book_kai_ticket(origin, destination)
    assert result in ["Daftar tiket berhasil ditampilkan", 
                      "Tidak ada tiket tersedia", 
                      "Tidak ada jadwal tersedia", 
                      "Hasil pencarian selesai dimuat"]

# Eksekusi langsung jika dijalankan sebagai script
if __name__ == "__main__":
    print(book_kai_ticket())