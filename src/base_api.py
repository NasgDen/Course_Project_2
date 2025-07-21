from abc import ABC, abstractmethod


class BaseApiClass(ABC):
    """Базовый абстрактный, определяющий интерфейс для работы с api запросами"""

    def __api_connect(self, *args, **kwargs):
        """Метод подключения к api hh.ru"""
        pass

    @abstractmethod
    def api_connection(self):
        self.__api_connect()

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """Метод для получения вакансий"""
        pass
