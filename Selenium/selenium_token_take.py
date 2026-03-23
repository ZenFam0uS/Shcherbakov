import time
import json
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")

login = driver.find_element("xpath","//input[@id='login_email']")
login.send_keys("zenjobs75476456@gmail.com")
time.sleep(1)
password = driver.find_element("xpath","//input[@id='password']")
password.send_keys("i@vUGzZxbEpqA4F")
time.sleep(1)
button_auth = driver.find_element("xpath","//button[@title='Отправить']")
button_auth.click()
time.sleep(1)

cookies = driver.get_cookies()
with open("cookies.json", 'w') as file:
    json.dump(cookies, file, indent=4)