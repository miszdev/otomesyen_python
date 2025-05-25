# tests/test_search_kai.py

def test_fill_and_search_ticket(kai_search_page):
    # Isi stasiun keberangkatan dan tujuan
    kai_search_page.fill_station_field("origination-flexdatalist", "GAMBIR")
    kai_search_page.fill_station_field("destination-flexdatalist", "YOGYAKARTA")

    # Pilih tanggal
    assert kai_search_page.select_date() is True

    # Cari tiket
    result = kai_search_page.search_tickets()
    print(f"Result: {result}")

    # Validasi hasil
    if result == "Daftar tiket berhasil ditampilkan":
        is_card_displayed = kai_search_page.driver.find_element_by_class_name("month-wrapper").is_displayed()
        assert is_card_displayed is True
    else:
        assert result in ["Tidak ada tiket tersedia", "Tidak ada jadwal tersedia", "Hasil pencarian selesai dimuat"]