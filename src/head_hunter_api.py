from src.base_api import BaseApiClass
import requests


class HeadHunterAPI(BaseApiClass):
    """ Класс для работы с api.hh.ru """
    name: str # наименование вакансии
    url: str # ссылка на вакансию
    salary: str # зарплата
    company: str # организация
    address: str # адрес организации


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
        return requests.get(url, params)

    def get_vacancies(self, name):
        return self.api_connect(name).json()




