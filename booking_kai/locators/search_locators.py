# locators/search_locators.py

class KaiSearchLocators:
    origination_field = ("id", "origination-flexdatalist")
    destination_field = ("id", "destination-flexdatalist")
    departure_date_field = ("id", "departure_dateh")
    submit_button = ("id", "submit")

    datepicker_wrapper = ("id", "ui-datepicker-div")
    holiday_date = ("xpath", '//td[@class=" holiday"]')
    available_date = ("xpath", 
        '//td[@data-handler="selectDay" and not(contains(@class, "ui-datepicker-unselectable"))]')

    schedule_list = ("class name", "schedule-list")
    alert_danger = ("xpath", "//div[contains(@class, 'alert-danger')]")
    empty_schedule = ("class name", "empty-schedule")
    loading_element = ("id", "loading")
    
    station_result = ("class name", "flexdatalist-results")