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
            EC.visibility_of_element_located(self.locator.STATION_RESULT)
        )
        field.send_keys(Keys.DOWN, Keys.ENTER)

    def select_date(self):
        date_picker = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator.DEPARTURE_DATE_FIELD)
        )
        date_picker.click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.locator.DATEPICKER_WRAPPER)
        )

        holidays = self.driver.find_elements(*self.locator.HOLIDAY_DATE)
        if holidays:
            holidays[0].click()
            return True

        available_dates = self.driver.find_elements(*self.locator.AVAILABLE_DATE)
        if available_dates:
            available_dates[0].click()
            return True

        return False

    def search_tickets(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.locator.SUBMIT_BUTTON)
        ).click()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.locator.SCHEDULE_LIST)
            )
            return "Daftar tiket berhasil ditampilkan"
        except TimeoutException:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(self.locator.LOADING_ELEMENT)
            )
            if self.driver.find_elements(*self.locator.ALERT_DANGER):
                return "Tidak ada tiket tersedia"
            elif self.driver.find_elements(*self.locator.EMPTY_SCHEDULE):
                return "Tidak ada jadwal tersedia"
            else:
                return "Hasil pencarian selesai dimuat"