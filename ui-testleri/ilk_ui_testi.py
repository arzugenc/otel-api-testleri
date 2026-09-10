import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Chrome tarayıcısını başlat
driver = webdriver.Chrome()

try:
    # 2. Test sayfasına git
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # 3. Form alanlarını doldur
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # 4. Giriş butonuna bas
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 5. Doğrulama (Assertion): Giriş başarılı mesajını kontrol et
    mesaj = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in mesaj
    print("TEST BASARILI: Kullanici basariyla giris yapti.")

    time.sleep(3)

finally:
    # 6. Tarayıcıyı kapat
    driver.quit()