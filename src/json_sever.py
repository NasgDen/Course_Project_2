from src.file_base_class import FileBaseClass
from src.utils import convert_object_to_dict
import json


class JSONSaver(FileBaseClass):
    """ Класс для работы с файлами формата JSON """

    def write_vacancy(self, filename, vacancies):
        """ Метод сохраняет список вакансий в файл формата JSON """

        list_json = convert_object_to_dict(vacancies)
        print(list_json)
        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(list_json, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, filename, vacancy):
        """ Метод записи данных в файл формата JSON"""
        with open(filename, mode="r", encoding="utf-8") as file:
            data_json = json.load(file)

        list_json = convert_object_to_dict(vacancy)
        data_json.extend(list_json)

        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    def read_vacancy(self):
        """ Метод чтения данных из файла """
        pass

    def delete_vacancy(self):
        """ Метод удаления данных из файла"""
        pass