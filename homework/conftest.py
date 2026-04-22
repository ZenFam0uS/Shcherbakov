import os # импорт модуля для работы с ос (переменные окружения, файлы-пути)

import pytest # импорт библиотеки для фикстурок
from selenium import webdriver # импорт вебдрайвера
# Скрываем определение автоматизации + отключаем модалки гугла
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")  # убирает флаг автоматизации
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # убирает баннер "controlled by automated software"
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)

@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) # ждёт до 10 сек появления элемента перед ошибкой
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def open_saucedemo(request):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com")
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def buy_saucedemo(request):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com")
    driver.find_element("xpath", "//input[@placeholder='Username']").send_keys("standard_user")
    driver.find_element("xpath", "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element("xpath", "//input[@name='login-button']").click()
    request.cls.driver = driver
    yield
    driver.quit()


#создание окружения
@pytest.fixture(autouse=True)
def setup_environment_properties():

    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"],
        "URL": os.environ["URL"],
        "PYTHON": os.environ["PYTHON"],
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")