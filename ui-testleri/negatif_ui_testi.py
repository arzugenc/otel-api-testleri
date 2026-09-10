import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Chrome tarayıcısını başlat
driver = webdriver.Chrome()

try:
    # 2. Test sayfasına git
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # 3. Form alanlarına doğru kullanıcı adı ve kasıtlı olarak HATALI şifre gönder
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("YanlisSifre123!")

    # 4. Giriş butonuna bas
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 5. Doğrulama (Assertion): Hata mesajı kutusundaki metni al ve kontrol et
    hata_mesaji = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in hata_mesaji
    print("TEST BASARILI: Yanlis sifre girildiginde beklenen hata mesaji goruntulendi.")

    time.sleep(2)

finally:
    # 6. Tarayıcıyı kapat
    driver.quit()