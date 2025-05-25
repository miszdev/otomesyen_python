from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def book_train_ticket(departure_station="JAKARTA", arrival_station="BANDUNG", holiday_index=0):
    """
    Mengotomatisasi pemesanan tiket kereta api di situs KAI
    
    Args:
        departure_station: Stasiun keberangkatan (default: "JAKARTA")
        arrival_station: Stasiun tujuan (default: "BANDUNG")
        holiday_index: Indeks hari libur yang dipilih (0 untuk pertama, dst)
    """
    # Setup dan konfigurasi browser
    driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait untuk semua pencarian elemen
    
    try:
        # Buka situs dan isi form awal
        print("Membuka situs Booking KAI...")
        driver.get("https://booking.kai.id/")
        
        # Fungsi helper untuk mengisi field dengan nilai dan memilih dari dropdown
        def fill_station_field(field_id, value):
            field = driver.find_element(By.ID, field_id)
            field.clear()
            field.send_keys(value)
            time.sleep(1)  # Jeda singkat untuk dropdown
            field.send_keys(Keys.DOWN, Keys.ENTER)
        
        # Isi stasiun keberangkatan dan tujuan
        print(f"Mengatur rute: {departure_station} → {arrival_station}")
        fill_station_field("origination-flexdatalist", departure_station)
        fill_station_field("destination-flexdatalist", arrival_station)
        
        # Buka pemilih tanggal
        driver.find_element(By.ID, "departure_dateh").click()
        
        # Temukan dan pilih hari libur
        def search_holidays():
            print("Mencari hari libur...")
            holiday = []
            
            # Cari sel dengan atribut title yang menandakan hari libur
            for cell in driver.find_elements(By.CSS_SELECTOR, "td[title]"):
                title = cell.get_attribute('title')
                if title:
                    if 'ui-datepicker-unselectable' not in cell.get_attribute('class'):
                        holiday.append((cell, cell.text, title))
            
            return holiday
        
        holiday = search_holidays()
        
        # Tampilkan dan pilih hari libur
        if holiday:
            print(f"Ditemukan {len(holiday)} hari libur:")
            for i, (_, tanggal, keterangan) in enumerate(holiday):
                print(f"  {i+1}. Tanggal {tanggal}: {keterangan}")
            
            if holiday_index < len(holiday):
                pilihan = holiday[holiday_index]
                print(f"Memilih: Tanggal {pilihan[1]}, {pilihan[2]}")
                pilihan[0].click()
            else:
                print(f"Indeks {holiday_index} tidak valid. Tersedia {len(holiday)} hari libur.")
                return
        else:
            print("Tidak ada hari libur tersedia di bulan ini.")
            return
        
        # Klik tombol cari
        print("Mencari kereta...")
        driver.find_element(By.ID, "submit").click()
        
        time.sleep(10)  # Waktu untuk melihat hasil
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Otomasi selesai.")

if __name__ == "__main__":
    book_train_ticket("JAKARTA", "BANDUNG", 0)  # Pemesanan tiket KAI dari JAKARTA ke BANDUNG, untuk hari libur