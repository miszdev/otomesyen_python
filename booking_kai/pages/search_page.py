# pages/search_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from locators.search_locators import KaiSearchLocators


class KaiSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = KaiSearchLocators

    def fill_station_field(self, field_id, value):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        field.clear()
        field.send_keys(value)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.locator.station_result)
        )
        field.send_keys(Keys.DOWN, Keys.ENTER)

    def select_date(self):
        date_picker = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator.departure_date_field)
        )
        date_picker.click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.locator.datepicker_wrapper)
        )

        holidays = self.driver.find_elements(*self.locator.holiday_date)
        if holidays:
            holidays[0].click()
            return True

        available_dates = self.driver.find_elements(*self.locator.available_date)
        if available_dates:
            available_dates[0].click()
            return True

        return False

    def search_tickets(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locator.submit_button)
        ).click()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.locator.schedule_list)
            )
            return "Daftar tiket berhasil ditampilkan"
        except TimeoutException:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.locator.loading_element)
            )
            if self.driver.find_elements(*self.locator.alert_danger):
                return "Tidak ada tiket tersedia"
            elif self.driver.find_elements(*self.locator.empty_schedule):
                return "Tidak ada jadwal tersedia"
            else:
                return "Hasil pencarian selesai dimuat"