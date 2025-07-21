from src.utils import (convert_object_to_dict, filter_vacancies,
                       get_top_vacancies, get_vacancies_by_salary,
                       print_vacancies, sort_vacancies)


def test_convert_object_to_dict(list_vacation, list_vacancy_test):
    assert convert_object_to_dict(list_vacation) == list_vacancy_test


def test_convert_object_to_dict_obj_vacancy(new_vacation, list_vacancy_test):
    assert convert_object_to_dict(new_vacation)[0] == list_vacancy_test[0]


def test_filter_vacancies(list_vacation):
    filter_vac = filter_vacancies(list_vacation, ["1234"])
    assert filter_vac[0].address == "Адрес 1234"


def test_get_vacancies_by_salary(list_vacation):
    filter_by_salary = list(get_vacancies_by_salary(list_vacation, ["40000", "110000"]))
    assert filter_by_salary[0].salary == "50000 - 100000"


def test_sort_vacancies(list_vacation_sort):
    assert sort_vacancies(list_vacation_sort) == list_vacation_sort


def test_get_top_vacancies(list_vacation_sort):
    assert get_top_vacancies(list_vacation_sort, 2) == list_vacation_sort


def test_print_vacancies(list_vacation_sort, capsys):
    print_vacancies(list_vacation_sort)
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == """Наименование :Python Developer
Ссылка на вакансию: https://hh.ru/vacancy/1234567
Диапазон зарплат: 50000 - 100000
Требования: Требования: опыт работы от 3 лет...
Обязанности: ответственность
Компания: Компания
Адрес: Адрес 4321
Наименование :Python QT
Ссылка на вакансию: https://hh.ru/vacancy/7654321
Диапазон зарплат: 100000 - 150000
Требования: Требования: опыт работы от 3 лет...
Обязанности: ответственность
Компания: Компания
Адрес: Адрес 1234"""
    )
