#pytest --alluredir=allure-resultspytest Pytest/test_alurte.py --alluredir=allure-results
#pytest --alluredir=allure-resultspytest Pytest/test_alurte.py --alluredir=allure-results --clean-alluredir # запускаем тест файла + сохраняем результаты в json директорию + чистим старые результаты + clean можно прокинуть в ini чтобы он выполнялся автоматически
#allure serve allure-results # запуск сервера для чтения директории
#export STAGE="Stage-1.qa" && export BROWSER="Chrome" && export MR="https://google.com" && export PYTHON="3.2.1" &&
#export STAGE="Stage-1.qa" && export BROWSER="Chrome" && export MR="https://google.com" && export PYTHON="3.2.1" && pytest --alluredir=allure-resultspytest Pytest/test_alurte.py --alluredir=allure-results --clean-alluredir

import pytest # команда для маркировки тестов
import allure # Импорт библиотеки allure для формирования отчетов и декораторов
from allure_commons.types import Severity
from allure_commons.types import AttachmentType # импорт для формирования скринов в тестах

# pip install pytest-rerunfailures команда для установки реранов тестов
# pytest -sv --reruns=2 кол-во реранов тестов
# pytest -sv --maxfail=2 кол-во падением тестов

@pytest.mark.usefixtures("driver")# Декоратор для использования фикстуры driver в каждом тесте класса
@allure.epic("Account") # Декоратор Allure для группировки тестов по эпику
@allure.feature("Login") #Декоратор Allure для указания фичи (функциональности)
@allure.story("Pages") # Декоратор Allure для указания пользовательской истории

class TestLesson:
    @allure.link(url="https://cunfluence.com/login", name="Documentation") #Декоратор Allure для добавления ссылки на документацию
    def test_open_login_page(self):

        with allure.step("Open login page"):self.driver.get("https://demoqa.com/login")
        # Прикрепляем скриншот текущей страницы к Allure отчету
        allure.attach(
            body = self.driver.get_screenshot_as_png(),
            name = "Login page",
            attachment_type=AttachmentType.PNG
        )
        with allure.step("Open assert login_page"):
            assert self.driver.current_url == "https://demoqa.com/login", "Ошибка: не верный переход на login"

    @pytest.mark.regression
    @allure.title("Open book page")
    @allure.severity(Severity.CRITICAL) #Декоратор Allure для установки степени критичности теста (CRITICAL)
    @allure.link(url="https://cunfluence.com/books", name="Documentation")
    def test_open_books_page(self): # падающий тест
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/boos", "Ошибка: не верный переход на books"

    @pytest.mark.regression
    @allure.title("Open profile page")
    @allure.severity(Severity.MINOR)
    @allure.link(url="https://cunfluence.com/profile", name="Documentation")
    def test_open_profile_page(self):
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка: не верный переход на profile"