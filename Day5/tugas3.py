from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Daftar website yang akan dicek titlenya
websites = [
    "tiket.com",
    "tokopedia.com",
    "orangsiber.com",
    "idejongkok.com",
    "kelasotomesyen.com"
]

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-minimized")  # Browser dimulai dalam keadaan minimize

# Inisialisasi WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Loop melalui setiap website
    for site in websites:
        url = f"https://{site}"
        try:
            # Buka website
            driver.get(url)
            # Tunggu sebentar agar halaman dimuat sepenuhnya
            time.sleep(2)
            # Ambil title
            title = driver.title
            # Tampilkan hasilnya
            print(f"{site} - {title}")
        except Exception as e:
            # Jika terjadi kesalahan, tampilkan domain dan pesan error
            print(f"{site} - Error: {str(e)}")

finally:
    # Tutup browser setelah selesai
    driver.quit()
    print("\nSelesai! Browser telah ditutup.")