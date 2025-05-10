from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://saucedemo.com')

# judul = driver.find_element(By.CLASS_NAME, 'login_logo').text
# print(judul)

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')

driver.find_element(By.ID, 'login-button').click()

# driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]') # relative xpath hasil copy
# driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button') # absolute xpath

# driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]').click() # rekomendasi
# driver.save_screenshot('screenshot.png')

# adtocartButton = driver.find_elements(By.CLASS_NAME, 'btn btn_primary btn_small btn_inventory ')
# print(adtocartButton)

adtocartButton = driver.find_elements(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
# print(adtocartButton)
# print(len(adtocartButton))
# addtocartButton[0].click()

for button in range(3):
    adtocartButton[button].click()

# for button in range(len(adtocartButton)):
#         adtocartButton[button].click()




# //*[@id="add-to-cart-sauce-labs-backpack"]
# /html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button