from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# chrome_driver_path = "/Users/ocean/chromedriver_mac_arm64/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# old version
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.amazon.com/CORSAIR-MK-2-Mechanical-Gaming-Keyboard/dp/B07D5S54C6/ref=sr_1_1?keywords=k70&qid=1674796195&sprefix=%2Caps%2C307&sr=8-1&th=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
driver.get("https://www.python.org/")
# doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a").text
# xpath_link = driver.find_element(
#     By.XPATH, """//*[@id="dive-into-python"]/ul[2]/li[1]/div[2]/h1""").text
list_event = driver.find_elements(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
dict_event = {}
for number in range(len(list_event)):
    time = list_event[number].find_element(
        By.TAG_NAME, "time").get_attribute("datetime").split("T")
    time = time[0]
    event_name = list_event[number].find_element(By.TAG_NAME, "a").text
    dict_event[number] = {
        'time': {time},
        'name': {event_name}
    }

print(dict_event)
