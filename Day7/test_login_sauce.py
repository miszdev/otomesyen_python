from selenium import webdriver
from selenium.webdriver.common.by import By

#testcase1: Login pake username dan password yang bener, maka akan masuk ke inventory page

def test_login():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=option)

    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get('https://saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    cur_url = driver.current_url
    assert cur_url == 'https://www.saucedemo.com/inventory.html'

    isCartButtonExist = driver.find_element(By.ID, 'shopping_cart_container').is_displayed()
    assert isCartButtonExist == True

    driver.close()