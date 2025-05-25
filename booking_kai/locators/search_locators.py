# locators/search_locators.py

class KaiSearchLocators:
    ORIGINATION_FIELD = ("id", "origination-flexdatalist")
    DESTINATION_FIELD = ("id", "destination-flexdatalist")
    DEPARTURE_DATE_FIELD = ("id", "departure_dateh")
    SUBMIT_BUTTON = ("id", "submit")

    DATEPICKER_WRAPPER = ("id", "ui-datepicker-div")
    HOLIDAY_DATE = ("xpath", '//td[@class=" holiday"]')
    AVAILABLE_DATE = ("xpath", 
        '//td[@data-handler="selectDay" and not(contains(@class, "ui-datepicker-unselectable"))]')

    SCHEDULE_LIST = ("class name", "schedule-list")
    ALERT_DANGER = ("xpath", "//div[contains(@class, 'alert-danger')]")
    EMPTY_SCHEDULE = ("class name", "empty-schedule")
    LOADING_ELEMENT = ("id", "loading")
    
    STATION_RESULT = ("class name", "flexdatalist-results")