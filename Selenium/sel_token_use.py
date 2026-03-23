import os.path
import time
from Selenium.cookies_manager import CookiesManager
from selenium import webdriver  # Импортируем основной компонент Selenium для управления браузером

login = ("xpath","//input[@id='login_email']")
password = ("xpath","//input[@id='password']")
button_auth = ("xpath","//button[@title='Отправить']")


driver = webdriver.Chrome()  # Запускаем браузер Chrome
driver.get("https://www.freeconferencecall.com/ru/ru/login")  # Открываем нужную страницу (важно зайти на домен перед добавлением кук)
cookies_manager = CookiesManager(driver)

if os.path.exists("cookies_manager.json"):
    cookies_manager.load()

else:
    driver.find_element(*login).send_keys("zenjobs75476456@gmail.com")
    driver.find_element(*password).send_keys("i@vUGzZxbEpqA4F")
    driver.find_element(*button_auth).click()
    cookies_manager.save()

time.sleep(5)


