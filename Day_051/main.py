from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys  # import keys ex: enter
import os
from time import sleep

my_email = os.environ.get("my_email")
my_pw = os.environ.get("my_pw")
PROMISED_DOWNLOAD_SPEED = 350
PROMISED_UPLOAD_SPEED = 250


class InternerSpeedTwitterBot():
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "detach", True)  # dont allow auto close
        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
        self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        start_btn = self.driver.find_element(By.CLASS_NAME, "start-button")
        start_btn.click()
        sleep(50)
        self.down_speed = self.driver.find_element(
            By.CSS_SELECTOR, ".download-speed.number").text
        self.up_speed = self.driver.find_element(
            By.CSS_SELECTOR, ".upload-speed.number").text
        if (float(self.down_speed) < PROMISED_DOWNLOAD_SPEED or float(self.up_speed) < PROMISED_UPLOAD_SPEED):
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login?lang=ko")
        sleep(1)
        email = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(my_email)
        email.send_keys(Keys.ENTER)
        sleep(1)
        try:
            ar = self.driver.find_element(
                By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            ar.send_keys("@oceanbrowser_")
            ar.send_keys(Keys.ENTER)
        except:
            pass

        sleep(1)
        pw = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pw.send_keys(my_pw)
        pw.send_keys(Keys.ENTER)
        sleep(2.5)
        tweet = self.driver.find_element(
            By.CLASS_NAME, 'DraftEditor-root')

        tweet.click()
        tweet = self.driver.find_element(
            By.CSS_SELECTOR, '.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        tweet.send_keys(
            f"claim!!! Internet speed \n upload speed:{self.up_speed} \n download speed:{self.down_speed} \n standard: (DOWN:{PROMISED_DOWNLOAD_SPEED}) (UP:{PROMISED_UPLOAD_SPEED})")
        post = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()

        sleep(1000)


InternerSpeedTwitterBot()
