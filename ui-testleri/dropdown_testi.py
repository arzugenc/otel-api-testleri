import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Dropdown test sayfasina git
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # 2. Dropdown elementini bul ve Selenium'un Select sinifina ver
    dropdown_element = driver.find_element(By.ID, "dropdown")
    secim = Select(dropdown_element)

    # 3. 'Option 2' secenegini sec
    secim.select_by_visible_text("Option 2")
    time.sleep(1)

    # 4. Dogrulama (Assertion): Secilen degerin gercekten 'Option 2' oldugunu teyit et
    secili_deger = secim.first_selected_option.text
    assert secili_deger == "Option 2"
    print("TEST BASARILI: Option 2 secildi ve dogrulandi.")

    # 5. 'Option 1' secenegini sec ve dogrula
    secim.select_by_visible_text("Option 1")
    time.sleep(1)
    assert secim.first_selected_option.text == "Option 1"
    print("TEST BASARILI: Option 1 secildi ve dogrulandi.")

finally:
    driver.quit()