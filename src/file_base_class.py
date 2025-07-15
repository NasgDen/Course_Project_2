from abc import ABC, abstractmethod


class FileBaseClass(ABC):
    """Базовый абстрактный класс, определяющий интерфейс работы с файлами"""

    @abstractmethod
    def add_vacancy(self):
        """ Метод записи данных в файл"""
        pass

    @abstractmethod
    def read_vacancy(self):
        """ Метод чтения данных из файла """
        pass

    @abstractmethod
    def delete_vacancy(self):
        """ Метод удаления данных из файла"""
        pass

