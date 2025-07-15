from abc import ABC, abstractmethod


class FileBaseClass(ABC):
    """Базовый абстрактный класс, определяющий интерфейс работы с файлами"""

    @abstractmethod
    def write_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """ Метод записи данных в файл"""
        pass

    @abstractmethod
    def read_vacancy(self, *args, **kwargs):
        """ Метод чтения данных из файла """
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        """ Метод удаления данных из файла"""
        pass

