from selenium.webdriver.common.by import By
from locators.inventory import Locator

class Inventory:
    def __init__(self, setup):
        self.setup = setup
        
    def check_cart_button(self):
        isCartButtonExist = self.setup.find_element(By.ID, Locator.btn_cart).is_displayed()
        assert isCartButtonExist == True