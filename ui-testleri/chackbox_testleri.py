

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

try:
    # 1. Sayfaya git
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Kutucukları bul
    kutular = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    kutu1 = kutular[0]
    kutu2 = kutular[1]

    # ADIM 1: Varsayılan durumları doğrula
    # (1. kutu boş olmalı, 2. kutu işaretli olmalı)
    assert not kutu1.is_selected(), "Hata: 1. kutu baslangicta secili geldi!"
    assert kutu2.is_selected(), "Hata: 2. kutu baslangicta secili degil!"
    print("BASARILI: Sayfa acildiginda varsayilan kutu durumlari dogrulandi.")

    # ADIM 2: 1. kutucuğu işaretle ve doğrula
    kutu1.click()
    assert kutu1.is_selected(), "Hata: 1. kutucuk isaretlenemedi!"
    print("BASARILI: 1. kutucuk tiklandi ve secildi.")

    # ADIM 3: 2. kutucuğun işaretini kaldır (uncheck) ve doğrula
    kutu2.click()
    assert not kutu2.is_selected(), "Hata: 2. kutucugun isareti kaldirilamadi!"
    print("BASARILI: 2. kutucuk tiklandi ve isareti kaldirildi.")

    time.sleep(1)

finally:
    driver.quit()