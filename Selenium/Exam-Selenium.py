import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Костыль для скипа модалки гугла
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")
time.sleep(1) # ждем чтобы сайт прогрузился

# Авторизация
user_name = driver.find_element("xpath","//input[@placeholder = 'Username']")
user_name.send_keys("standard_user")

password_user = driver.find_element("xpath","//input[@id='password']")
password_user.send_keys("secret_sauce")

button_auth = driver.find_element("xpath","//input[@name = 'login-button']")
button_auth.click()
time.sleep(1)# ждем время после авторизации

# Проверка того что страница сменилась при авторизации
assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Авторизация не выполнена"

print("Авторизация прошла успешно")

# Добавление карточки товара в корзину
button_price = driver.find_element("xpath","//button[@data-test='add-to-cart-sauce-labs-backpack']")
button_price.click()

time.sleep(0.30) # даю время на отображение товара в корзине

# Проверка изменения кнопки с Add-to-cart на Remove
# Ищем кнопку с атрибутом data-test='remove-sauce-labs-backpack'
remove_button = driver.find_elements("xpath", "//button[@data-test='remove-sauce-labs-backpack']")

if remove_button:
    # Проверяем, что текст на кнопке соответствует "Remove"
    button_text = remove_button[0].text
    assert button_text == "Remove", f"Ожидался текст 'Remove', получено '{button_text}'"
    print(f"Кнопка успешно изменилась на Remove. Текст: {button_text}")
else:
    print("Кнопка Remove не найдена")
    assert False, "Кнопка не изменилась с Add-to-cart на Remove"

# Проверяем наличие счетчика корзины
cart_badge = driver.find_elements("class name", "shopping_cart_badge") # делаем поиск по всем локатором с class = shopping_cart_badge и записываю их в переменную cart_badge

if cart_badge:
    badge_text = cart_badge[0].text # берем элемент списка (так как он у нас единственный) и извлекаем текст внутри сохраняя в переменную
    assert badge_text == "1", f"Ожидалось 1, получено {badge_text}" # проверка, что при добавлении 1 элемента будет отображаться число 1
    print(f"Товар добавлен в корзину. Кол-во: {badge_text}")
else:
    print("Счетчик корзины не найден")
    assert False, "Счетчик корзины отсутствует"

# Ищем корзинку и проваливаемся туда
basket = driver.find_element("xpath","//*[@data-test='shopping-cart-link']")
basket.click()

time.sleep(1)

# Проверяем что url изменился при переходе
assert driver.current_url == "https://www.saucedemo.com/cart.html", "Переход в корзину не отработал"
print("Переход на страницу покупок осуществлен")

time.sleep(1)

# Получаем все товары в корзине
cart_products = driver.find_elements("class name", "inventory_item_name")
product_names = [product.text for product in cart_products]

print(f"Товары в корзине: {product_names}")
print(f"Количество товаров: {len(product_names)}")

# Проверка 1: количество товаров должно быть равно 1
assert len(product_names) == 1, f"Ожидался 1 товар в корзине, но найдено {len(product_names)}"

# Проверка 2: проверяем, что это именно Sauce Labs Backpack
assert product_names[0] == "Sauce Labs Backpack", f"Ожидался товар 'Sauce Labs Backpack', но найден '{product_names[0]}'"

# Проверка 3: дополнительно проверяем, что нет других товаров (явно проверяем, что список не содержит других названий)
unexpected_products = [name for name in product_names if name != "Sauce Labs Backpack"]
assert len(unexpected_products) == 0, f"Найдены лишние товары: {unexpected_products}"

print(f"Проверка пройдена: в корзине ровно 1 товар - Sauce Labs Backpack")

continue_check = driver.find_element("xpath","//button[@data-test = 'checkout']")
continue_check.click()

assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Переход на страницу уточнения данных не осуществлен"
print("Переход на страницу уточнения данных осуществлен")

# Нажимаем кнопку при пустых полях проверяя негативный кейс
continue_button = driver.find_element("xpath","//input[@data-test = 'continue']")
continue_button.click()

# Проверяем что при пустых инпутах переход не осуществился
assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Осуществлен переход без вводимых данных"
print("Переход на другую страницу не осуществлен пока данные не ввелись")

# Проверяем что подсказка появилась
error_message = driver.find_elements("xpath", "//h3[@data-test='error']") # поиск по всем эелементам с указанным локатором

if error_message:
    error_text = error_message[0].text
    print(f"Сообщение об ошибке: {error_text}")
    assert error_text == "Error: First Name is required", f"Ожидалось 'Error: First Name is required', получено '{error_text}'"
    print("Проверка пройдена: сообщение об ошибке отобразилось корректно")
else:
    print("Сообщение об ошибке не найдено")
    assert False, "Ошибка 'First Name is required' не появилась"

# Вводим информацию пользователя
first_name_user = driver.find_element("xpath","//input[@name = 'firstName']")
first_name_user.send_keys("Test")
time.sleep(0.3)
last_name_user = driver.find_element("xpath","//input[@name = 'lastName']")
last_name_user.send_keys("Testovich")
time.sleep(0.3)
post_code_user = driver.find_element("xpath","//input[@name = 'postalCode']")
post_code_user.send_keys("320530")
time.sleep(0.3)

# Идем дальше
continue_button = driver.find_element("xpath","//input[@data-test = 'continue']")
continue_button.click()
assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Переход на шаг 2 не осуществился"
print("Осуществлен переход на шаг 2")

time.sleep(0.3)

finish_button = driver.find_element("xpath","//button[@data-test = 'finish']")
finish_button.click()
assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "Переход на экран успешности не осуществлен"
print("Поздравляем, покупка удачна!")

time.sleep(0.3)

home_button = driver.find_element("xpath","//button[@data-test = 'back-to-products']")
home_button.click()
print("Кнопка Back Home доступна для нажатия")
assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Переход на главный экран не осуществился"
print("Переход на главный экран выполнен")