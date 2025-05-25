import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    # Setup WebDriver dengan Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()  # Maksimalkan jendela browser
    yield driver
    driver.quit()  # Tutup browser setelah test selesai

def test_open_booking_kai(driver):
    # Buka website
    driver.get("https://booking.kai.id/")
    
    # Tunggu hingga elemen tertentu muncul untuk memastikan halaman dimuat
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Selamat Datang di KAI Access')]"))
    )
    
    # Verifikasi judul halaman
    assert driver.title == "KAI Access - PT KAI", f"Expected title 'KAI Access - PT KAI', but got '{driver.title}'"
    
    # Verifikasi elemen teks tertentu ada di halaman
    welcome_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Selamat Datang di KAI Access')]")
    assert welcome_text.is_displayed(), "Welcome text is not visible"