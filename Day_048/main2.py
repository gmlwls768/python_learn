from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys  # import keys ex: enter

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # dont allow auto close

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
# source_view = driver.find_element(By.LINK_TEXT, "View source")
# source_view.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

driver.get("https://www.getresponse.com/start-free")
name = driver.find_element(By.ID, "startFreeTrial_firstName")
name.send_keys("ocean")
email = driver.find_element(By.ID, "startFreeTrial_email")
email.send_keys("ocean@example.com")
pw = driver.find_element(By.ID, "startFreeTrial_password")
pw.send_keys("Abxdexample!!!1")
pw.send_keys(Keys.ENTER)
