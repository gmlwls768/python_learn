from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys  # import keys ex: enter
import os
from time import sleep
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PW = os.environ.get("MY_PW")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # dont allow auto close
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3299474939&f_LF=f_AL&geoId=105149562&keywords=python%20developer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&refresh=true")
login_tab = driver.find_element(By.LINK_TEXT, "로그인")
login_tab.click()
sleep(1)
login_email = driver.find_element(By.ID, "username")
login_email.send_keys(MY_EMAIL)
login_pw = driver.find_element(By.ID,  "password")
login_pw.send_keys(MY_PW)
login_pw.send_keys(Keys.ENTER)

try:
    pass_login = driver.find_element(By.LINK_TEXT, "건너뛰기")
    pass_login.click()
except:
    pass
sleep(1)
job_container = driver.find_elements(
    By.CLASS_NAME, "jobs-search-results__list-item")
for job in job_container:
    sleep(0.5)
    job.click()
    sleep(0.5)
    job_save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    job_save.click()
    sleep(0.7)
    job_follow = driver.find_element(By.CLASS_NAME, "follow   ")
    job_follow.send_keys(Keys.ENTER)
