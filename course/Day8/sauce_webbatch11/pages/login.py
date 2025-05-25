from selenium.webdriver.common.by import By
from locators.login import Locator

class Login:
    def __init__(self, setup):
        self.setup = setup
    
    def input_username(self, username):
        self.setup.find_element(By.ID, Locator.input_username).send_keys(username)
        
    def input_password(self, password):
        self.setup.find_element(By.ID, Locator.input_password).send_keys(password)

    def click_login(self):
        self.setup.find_element(By.ID, Locator.btn_login).click()
    
    def check_error_message(self):    
        
        error_message = self.setup.find_element(By.XPATH,Locator.err_message).text
        
        return error_message