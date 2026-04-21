from selenium import webdriver


class Testlesson:

    def setup_method(self):# метод позволяет выполнять условия перед тестами

        self.driver = webdriver.Chrome()

    def test_open_login_page(self):

        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка: не верный переход"

    def teardown_method(self): # метод позволяет выполять условия после теста
        self.driver.quit()

