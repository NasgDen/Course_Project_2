from src.base_api import BaseApiClass
import requests


class HeadHunterAPI(BaseApiClass):
    """ Класс для работы с api.hh.ru """

    def __init__(self):
        """ Инициализация атрибутов класса """
        pass

    def api_connect(self, name):
        """ Метод подключения к api.hh.ru """
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": name,
            "period": 3
        }
        response = requests.get(url, params)
        if response.status_code == 200:
            return response
        else:
            return {}

    def get_vacancies(self, name):
        """ Получение вакансий с hh.ru в формате JSON """
        result = self.api_connect(name).json()
        return result




