from src.base_api import BaseApiClass
import requests


class HeadHunterAPI(BaseApiClass):
    """Класс для работы с api.hh.ru"""

    __url = "https://api.hh.ru/vacancies"
    __params = {}

    def __init__(self):
        """Инициализация атрибутов класса"""
        pass

    def __api_connect(self, name):
        """Приватный Метод подключения к api.hh.ru"""
        self.__params = {"text": name, "period": 3}
        response = requests.get(self.__url, self.__params)
        if response.status_code == 200:
            return response
        else:
            return {}

    def api_connection(self):
        return self.__api_connect()

    def get_vacancies(self, name):
        """Получение вакансий с hh.ru в формате JSON"""
        result = self.__api_connect(name).json()
        return result
