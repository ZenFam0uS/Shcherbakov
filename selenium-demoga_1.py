import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

user_name_field = driver.find_element("xpath", "//input[@id='userName']")

user_name_field.send_keys("admin")

email_field = driver.find_element("xpath", "//input[@id='userEmail']")

email_field.send_keys("test@gmail.com")

address_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")

address_field.send_keys("Старый Оскол, ул. Широкая, д.41")

time.sleep(5)
