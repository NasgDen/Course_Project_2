from abc import ABC, abstractmethod


class FileBaseClass(ABC):
    """Базовый абстрактный класс, определяющий интерфейс работы с файлами"""

    def write(self):
        """ Метод записи данных в файл"""
        pass


    def read(self):
        """ Метод чтения данных из файла """
        pass


    def delete(self):
        """ Метод удаления данных из файла"""
        pass

