from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time  # for delay

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # dont allow auto close

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
select_lang = driver.find_element(By.ID, "langSelect-KO")
select_lang.click()
time.sleep(4)
cookie_btn = driver.find_element(By.ID, "bigCookie")
timeout = time.time()+5
five_min = time.time()+60*5
while True:
    cookie_btn.click()

    if time.time() > timeout:
        try:
            upgrades = driver.find_elements(
                By.CSS_SELECTOR, "#upgrades .enabled")
            upgrades[-1].click()
        except:
            print("No upgrades available")

        try:
            products = driver.find_elements(
                By.CSS_SELECTOR, "#products .enabled")
            products[-1].click()
        except:
            print("No upgrades available")

        # try:
        #     for num in range(10):
        #         enable_product = driver.find_element(
        #             By.ID, f'productPrice{num}')
        #         price = driver.find_element(By.ID, "cookies")
        #         price = price.text.split("쿠키")[0]
        #         enable_product_text = enable_product.text
        #         if price.find(","):
        #             price = price.replace(",", "")
        #         if enable_product_text.find(","):
        #             enable_product_text = enable_product_text.replace(",", "")
        #         if int(price) < int(enable_product_text):
        #             raise

        # except:
        #     try:
        #         enable_product = driver.find_element(
        #             By.ID, f'product{num-1}')
        #         enable_product.click()
        #     except:
        #         pass
        finally:
            timeout = time.time() + 5

    if five_min < time.time():
        per_sec_cookie = driver.find_element(By.ID, "cookiesPerSecond")
        print(per_sec_cookie.text)
        break
