from selenium import webdriver
import pytest # команда для маркировки тестов

# pip install pytest-rerunfailures команда для установки реранов тестов
# pytest -sv --reruns=2 кол-во реранов тестов
# pytest -sv --maxfail=2 кол-во падением тестов

class Testlesson:

    def setup_method(self):# метод позволяет выполнять условия перед тестами

        self.driver = webdriver.Chrome()

    @pytest.mark.smoke
    def test_open_login_page(self):

        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка: не верный переход на login"

    @pytest.mark.regression
    def test_open_books_page(self): # падающий тест

        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/boos", "Ошибка: не верный переход на books"

    @pytest.mark.regression
    def test_open_profile_page(self):

        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка: не верный переход на profile"

    def teardown_method(self): # метод позволяет выполять условия после теста
        self.driver.quit()
