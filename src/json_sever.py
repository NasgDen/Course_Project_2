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

        data_json = self.read_vacancy(filename)
        list_json = convert_object_to_dict(vacancy)
        data_json.extend(list_json)
        print(data_json)

        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    def read_vacancy(self, filename):
        """ Метод чтения данных из файла """
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                data_json = json.load(file)
        except FileNotFoundError as err:
            data_json = []
        return data_json

    def delete_vacancy(self, filename, vacancy):
        """ Метод удаления данных из файла"""

        data_json = self.read_vacancy(filename)

        list_json = convert_object_to_dict(vacancy)
        print(list_json)
        index = 0
        delet_data = {}
        for data in data_json:
            for vacancy in list_json:
                if data.get("name") == vacancy.get("name"):
                    delet_data =  data_json.pop(index)
                else:
                    index += 1
        print(len(delet_data))
        if len(delet_data) > 0:
            print("Запись успешна удалена")
            with open(filename, mode="w", encoding="utf-8") as file:
                json.dump(data_json, file, indent=4, ensure_ascii=False)
        else:
            print("Запись не найдена")