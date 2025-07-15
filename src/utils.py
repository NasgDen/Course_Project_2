import json
from src.vacancy import Vacancy


def write_json_file(data, file_name: str) -> None:
    """Запись данных в файл формата json"""
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def convert_object_to_dict(vacancies):
    """ Конвертация объектов класса Vacancy в список словарей """
    list_json = []
    if isinstance(vacancies, list):
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
    elif isinstance(vacancies, Vacancy):
        to_dict = {}
        to_dict["name"] = vacancies.name
        to_dict["url"] = vacancies.url
        to_dict["salary"] = vacancies.salary
        to_dict["requirement"] = vacancies.requirement
        to_dict["responsibility"] = vacancies.responsibility
        to_dict["company"] = vacancies.company
        to_dict["address"] = vacancies.address
        list_json.append(to_dict)
    return list_json
