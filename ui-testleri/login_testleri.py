import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

try:
    
    #  Geçersiz Kullanıcı Adı ile Giriş Denemesi
    # -------------------------------------------------------------
    print("\n--- Test 1: Gecersiz Kullanici Adi Deneniyor ---")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("hatali_kullanici")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    mesaj = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in mesaj
    print("BASARILI: Gecersiz kullanici adi hatasi teyit edildi.")

    # -------------------------------------------------------------
    # Boş Alan Bırakılarak Giriş Denemesi
    # -------------------------------------------------------------
    print("\n--- Test 2: Bos Form Deneniyor ---")
    driver.get("https://the-internet.herokuapp.com/login")
    # Form alanlarina hicbir sey yazmadan dogrudan Login butonuna bas
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    mesaj = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in mesaj
    print("BASARILI: Bos form gonderiminde sistemin hata verdigi dogrulandi.")

    # -------------------------------------------------------------
    #  Başarılı Giriş ve Güvenli Çıkış (Logout) Akışı
    # -------------------------------------------------------------
    print("\n--- Test 3: Giris ve Logout Akisi Deneniyor ---")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    
    assert "You logged into a secure area!" in driver.find_element(By.ID, "flash").text


    driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()

    cikis_mesaji = driver.find_element(By.ID, "flash").text
    assert "You logged out of the secure area!" in cikis_mesaji
    print("BASARILI: Kullanici cikis yapti ve giris sayfasina yonlendirildi.")

    time.sleep(2)

finally:
    driver.quit()