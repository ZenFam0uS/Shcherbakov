#Это База
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# #Опции
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
#
FILE_UPLOADE_FIELD = ("xpath","//input[@id = 'uploadFile']")
# #Инициализация
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")

file_field = driver.find_element(*FILE_UPLOADE_FIELD)
file_field.send_keys(r"C:\Users\kaz0n\Desktop\TEST_PYTON_file.txt")

time.sleep(2)