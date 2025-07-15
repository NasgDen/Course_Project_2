from src.file_base_class import FileBaseClass
import json


class JSONSaver(FileBaseClass):
    """ Класс для работы с файлами формата JSON """

    def write_vacancy(self, filename, vacancies):
        """ Метод сохраняет список вакансий в файл формата JSON """

        list_json = []

        for data in vacancies:
            to_dict = {}
            to_dict["name"] = data.name
            to_dict["url"] = data.url
            to_dict["salary"] = data.salary
            to_dict["requirement"] = data.requirement
            to_dict["responsibility"] = data.responsibility
            to_dict["company"] = data.company
            to_dict["address"] = data.address

            list_json.append(to_dict)

        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(list_json, file, indent=4, ensure_ascii=False)

    def add_vacancy(self):
        """ Метод записи данных в файл"""
        pass

    def read_vacancy(self):
        """ Метод чтения данных из файла """
        pass

    def delete_vacancy(self):
        """ Метод удаления данных из файла"""
        pass