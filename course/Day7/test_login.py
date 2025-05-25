import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Daftar skenario pengujian
# Format: (username, password, expected_url, should_cart_exist)
login_scenarios = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html', True),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/', False),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html', True),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html', True),
    ('standard_user', 'wrong_password', 'https://www.saucedemo.com/', False),
    ('', 'secret_sauce', 'https://www.saucedemo.com/', False),
    ('standard_user', '', 'https://www.saucedemo.com/', False),
]

@pytest.fixture
def driver():
    """Fixture untuk menyiapkan dan membersihkan driver."""
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    # Headless mode untuk testing otomatis
    # option.add_argument('--headless')
    
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Berikan driver ke test
    yield driver
    
    # Bersihkan setelah selesai
    driver.quit()

@pytest.mark.parametrize('username, password, expected_url, should_cart_exist', login_scenarios)
def test_login_scenarios(driver, username, password, expected_url, should_cart_exist):
    """Test berbagai skenario login dengan parameter berbeda."""
    # Buka halaman login
    driver.get('https://www.saucedemo.com')
    
    # Isi form login
    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    
    # Verifikasi URL sesuai ekspektasi
    cur_url = driver.current_url
    assert cur_url == expected_url, f"Expected URL {expected_url}, but got {cur_url}"
    
    # Verifikasi keberadaan tombol keranjang jika seharusnya ada
    if should_cart_exist:
        isCartButtonExist = driver.find_element(By.ID, 'shopping_cart_container').is_displayed()
        assert isCartButtonExist == True, "Shopping cart button should be visible"

# Test untuk skenario login yang berhasil
def test_successful_login(driver):
    """Test untuk skenario login yang berhasil dengan validasi tambahan."""
    # Buka halaman login
    driver.get('https://www.saucedemo.com')
    
    # Isi form login
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    
    # Verifikasi URL
    cur_url = driver.current_url
    assert cur_url == 'https://www.saucedemo.com/inventory.html'
    
    # Verifikasi elemen-elemen di halaman inventory
    isCartButtonExist = driver.find_element(By.ID, 'shopping_cart_container').is_displayed()
    assert isCartButtonExist == True
    
    # Verifikasi bahwa judul halaman benar
    page_title = driver.find_element(By.CLASS_NAME, 'title').text
    assert page_title == 'Products', f"Expected page title 'Products', but got '{page_title}'"
    
    # Verifikasi bahwa minimal ada 1 produk yang ditampilkan
    inventory_items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(inventory_items) > 0, "No inventory items found"