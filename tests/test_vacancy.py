from src.vacancy import Vacancy


def test_init_vacation(new_vacation):
    assert new_vacation.name == "Python Developer"
    assert new_vacation.url == "https://hh.ru/vacancy/1234567"
    assert new_vacation.salary == "100000 - 150000"
    assert new_vacation.requirement == "Требования: опыт работы от 3 лет..."
    assert new_vacation.responsibility == "ответственность"
    assert new_vacation.company == "Компания"
    assert new_vacation.address == "Адрес 4321"


def test_lt_vacation(list_vacation):
    assert list_vacation[0] > list_vacation[1]


def test_cast_to_object_list(response):
    result = [
        Vacancy(
            "name",
            "https://hh.ru/vacancy/122842251",
            "10 - 50",
            "requirement",
            "responsibility",
            "name",
            "raw",
        )
    ]
    vacancy_list = Vacancy.cast_to_object_list(response)
    assert vacancy_list[0].name == result[0].name
    assert vacancy_list[0].url == result[0].url
    assert vacancy_list[0].salary == result[0].salary
    assert vacancy_list[0].requirement == result[0].requirement
    assert vacancy_list[0].responsibility == result[0].responsibility
    assert vacancy_list[0].company == result[0].company
    assert vacancy_list[0].address == result[0].address
