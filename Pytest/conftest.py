import os

import pytest
from selenium import webdriver

@pytest.fixture()

def driver(request):

    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield # все что до, это предварительная настройка (yield передает управление в тестовую ф-ию)
    driver.quit() #закрытие работы драйвера (закрытие браузера)


#создание окружения
@pytest.fixture(autouse=True)
def setup_environment_properties():

    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"],
        "MR": os.environ["MR"],
        "PYTHON": os.environ["PYTHON"],
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")