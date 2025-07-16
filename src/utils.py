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


def filter_vacancies(vacancy: list[Vacancy], filter_words: str):
    """ Функция фильтрует список вакансий по заданым словам"""

    vacancy_filter = filter(lambda x: filter_words in x.name, vacancy)
    return vacancy_filter


def get_vacancies_by_salary(vacancy: list[Vacancy], salary_range: list):
    """ Функция фильтрует список вакансий по диапазону зарплат"""
    vacancy_filter = filter(lambda x: (salary_range[0] < (x.salary.split(" - "))[0]) and (salary_range[1] > (x.salary.split(" - "))[1]), vacancy)
    # for i in vacancy_filter:
    #     print(i)
    return vacancy_filter


def sort_vacancies(vacancy: list[Vacancy]):
    """ Функция сортирует список вакансий по минимальной зарплате по убыванию"""

    vacancy_sorted = sorted(vacancy, key=lambda p: p.salary.split(" - ")[0], reverse=True)
    print(f"Найдено и отсортировано вакансий: {len(vacancy_sorted)} шт.")
    return vacancy_sorted

def get_top_vacancies(vacancy: list[Vacancy], top_n):
    if len(vacancy) < top_n:
        return vacancy
    else:
        return vacancy[:top_n]



