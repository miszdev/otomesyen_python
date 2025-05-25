import pytest
from pages.login import Login
from pages.inventory import Inventory
from dotenv import load_dotenv
import os

load_dotenv()
#testcase1: Login pake username dan password yang bener, maka akan masuk ke inventory page
def test_login(setup):
    login = Login(setup)
    inventory = Inventory(setup)
    
    usrname = os.getenv('USERNAME')
    pwd = os.getenv('PASSWORD')

    login.input_username(usrname)
    login.input_password(pwd)
    login.click_login()

    cur_url = setup.current_url
    assert cur_url == 'https://www.saucedemo.com/inventory.html'
    
    inventory.check_cart_button()
    
    
'''
username bener, passwordnya salah -> error message
username salah, passwordnya bener -> error message
username salah, passwordnya salah -> error message
username kosong, passwordnya bener -> error message
username bener, passwordnya kosong -> error message
'''

data_login = [
            ('standard_user', 'passwordsalah', 'Epic sadface: Username and password do not match any user in this service'),
            ('salahusername', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service'),
            ('salahusername', 'passwordsalah', 'Epic sadface: Username and password do not match any user in this service'),
            ('', 'secret_sauce', 'Epic sadface: Username is required'),
            ('standard_user', '', 'Epic sadface: Password is required')
            ]

@pytest.mark.parametrize('username, password, error', data_login)
def test_negative_login(username, password, error, setup):
    login = Login(setup)

    login.input_username(username)
    login.input_password(password)
    login.click_login()    

    error_message = login.check_error_message()
    
    assert error_message == error

    
''' 
Precondition / Set up - Steps automation yang dilakukan sebelum skenario utama dijalankan 

buka browser
set option (max window, minimize, set timeout / implicitlywait.. hit api,)
Login -> Skenario utama

Postcondition / Tear Down - Steps automation yang dilakukan setelah skenario utama dijalankan 

contoh: close browser, clear cache, hit api xxxxx

'''