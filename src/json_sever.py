import json
import os

from src.file_base_class import FileBaseClass
from src.utils import convert_object_to_dict
from src.vacancy import Vacancy

PATH_TO_FILE = os.path.join("data", "vacancy.json")


class JSONSaver(FileBaseClass):
    """Класс для работы с файлами формата JSON"""

    __filename: str

    def __init__(self, filename=PATH_TO_FILE):
        self.__filename = os.path.join(filename)
        print(self.__filename)

    def write_vacancy(self, vacancies: list[Vacancy]) -> None:
        """Метод сохраняет список вакансий в файл формата JSON"""

        list_json = convert_object_to_dict(vacancies)
        with open(self.__filename, mode="w", encoding="utf-8") as file:
            json.dump(list_json, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy: list[Vacancy]) -> None:
        """Метод записи данных в файл формата JSON"""

        data_json = self.read_vacancy()

        list_json = convert_object_to_dict(vacancy)

        index = 0
        for vac in list_json:
            for data in data_json:
                if data.get("url") == vac.get("url"):
                    index += 1
                    print("Вакансия не добавлена. Данная вакансия уже существует")
        if index == 0:
            data_json.extend(list_json)
            print("Вакансия добавлена")
            print(data_json)

        with open(self.__filename, mode="w", encoding="utf-8") as file:
            json.dump(data_json, file, indent=4, ensure_ascii=False)

    def read_vacancy(self):
        """Метод чтения данных из файла"""
        try:
            with open(self.__filename, mode="r", encoding="utf-8") as file:
                data_json = json.load(file)
        except FileNotFoundError as err:
            data_json = []
        return data_json

    def delete_vacancy(self, vacancy: list[Vacancy]) -> None:
        """Метод удаления данных из файла"""

        data_json = self.read_vacancy()

        list_json = convert_object_to_dict(vacancy)
        index = 0
        delet_data = {}
        for data in data_json:
            for vacancy in list_json:
                if data.get("name") == vacancy.get("name"):
                    delet_data = data_json.pop(index)
                else:
                    index += 1
        if len(delet_data) > 0:
            print("Запись успешна удалена")
            with open(self.__filename, mode="w", encoding="utf-8") as file:
                json.dump(data_json, file, indent=4, ensure_ascii=False)
        else:
            print("Запись не найдена")
