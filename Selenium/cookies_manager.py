import json  # Импортируем модуль для работы с JSON-файлами
from selenium.webdriver.chrome.webdriver import \
    WebDriver  # Импортируем тип данных WebDriver для подсказок (тайп-хинтинга)


class CookiesManager:  # Объявляем класс для управления куками

    def __init__(self, driver, file_path="cookies.json"):  # Конструктор класса: принимает драйвер и путь к файлу
        self.driver: WebDriver = driver  # Сохраняем экземпляр драйвера внутри класса
        self.file_path = file_path  # Сохраняем путь к файлу, где лежат куки

    def save(self):  # Метод для сохранения текущих кук из браузера в файл
        cookies = self.driver.get_cookies()  # Получаем список всех кук из открытого браузера
        with open(self.file_path, "w") as file:  # Открываем файл на запись
            json.dump(cookies, file, indent=4)  # Записываем куки в файл в красивом формате (отступ 4 пробела)

    def load(self):  # Метод для загрузки кук из файла в браузер
        self.driver.delete_all_cookies()  # Полностью очищаем текущие куки браузера
        with open(self.file_path, "r") as file:  # Открываем файл с куками на чтение
            cookies = json.load(file)  # Читаем данные из файла и превращаем их в список Python
        for cookie in cookies:  # Перебираем каждую куку в цикле
            self.driver.add_cookie(cookie)  # Добавляем куку в текущую сессию браузера
        self.driver.refresh()  # Обновляем страницу, чтобы сайт применил новые куки и авторизовал нас