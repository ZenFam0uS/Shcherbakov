import time
from selenium import webdriver # импорт самого веб драйвера
from selenium.webdriver.common.keys import Keys #импорт комбинации клавиш

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/key_presses")
# driver.get("https://demoqa.com/text-box") # сайт
#
# user_name_field = driver.find_element("xpath", "//input[@id='userName']") # навигатор
#
# user_name_field.send_keys("admin") # данные для ввода
#
# # time.sleep(2)
# #
# # user_name_field.clear() # очистка поля с помощью команды
#
# email_field = driver.find_element("xpath", "//input[@id='userEmail']")
#
# email_field.send_keys("test@gmail.com")
#
# address_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")
#
# address_field.send_keys("Старый Оскол, ул. Широкая, д.41")
#
# # assert user_name_field.get_attribute("value") == "admin", "Error"
#
# time.sleep(5)


# filed = driver.find_element("xpath","//input[@id='target']")
#
# filed.send_keys("HELLO WORLD")
#
# time.sleep(1)
#
# filed.send_keys(Keys.CONTROL+"A")
# time.sleep(1)
#
# filed.send_keys(Keys.BACKSPACE)
#
# time.sleep(1)

driver.get("https://www.randomtextgenerator.com")
time.sleep(1)

random_text_field = driver.find_element("xpath", "//body")

random_text_field.send_keys(Keys.CONTROL+"a")
time.sleep(1)
random_text_field.send_keys(Keys.CONTROL+"c")
time.sleep(1)

driver.get("https://demoqa.com/text-box")

current_text_field = driver.find_element("xpath","//textarea[@id='currentAddress']")
time.sleep(1)

current_text_field.send_keys(Keys.CONTROL+"v")
time.sleep(10)
