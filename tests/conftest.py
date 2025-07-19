import pytest
from src.vacancy import Vacancy

@pytest.fixture()
def new_vacation():
    return Vacancy(
        "Python Developer",
        "https://hh.ru/vacancy/1234567",
        "100000 - 150000",
        "Требования: опыт работы от 3 лет...",
        "ответственность",
        "Компания",
        "Адрес 4321",
    )

@pytest.fixture()
def list_vacation():
    return [
        Vacancy(
            "Python Developer",
            "https://hh.ru/vacancy/1234567",
            "100000 - 150000",
            "Требования: опыт работы от 3 лет...",
            "ответственность",
            "Компания",
            "Адрес 4321",
        ),
        Vacancy(
            "Python QT",
            "https://hh.ru/vacancy/7654321",
            "50000 - 100000",
            "Требования: опыт работы от 3 лет...",
            "ответственность",
            "Компания",
            "Адрес 1234",
        )
    ]

@pytest.fixture()
def response():
    return {"items":
                  [{"name": "name",
                   "alternate_url": "https://hh.ru/vacancy/122842251",
                   "salary":
                       {
                           "from": "10",
                           "to": "50"
                       },
                   "snippet":
                       {
                            "requirement": "requirement",
                            "responsibility": "responsibility"
                       },
                   "employer":
                       {
                           "name": "name"
                       },
                   "address":
                       {
                           "raw": "raw"
                       }
                   }]
    }


@pytest.fixture()
def list_vacancy_test():
    return [{'name': 'Python Developer', 'url': 'https://hh.ru/vacancy/1234567', 'salary': '100000 - 150000', 'requirement': 'Требования: опыт работы от 3 лет...', 'responsibility': 'ответственность', 'company': 'Компания', 'address': 'Адрес 4321'}, {'name': 'Python QT', 'url': 'https://hh.ru/vacancy/7654321', 'salary': '50000 - 100000', 'requirement': 'Требования: опыт работы от 3 лет...', 'responsibility': 'ответственность', 'company': 'Компания', 'address': 'Адрес 1234'}]


@pytest.fixture()
def list_vacation_sort():
    return [
        Vacancy(
            "Python Developer",
            "https://hh.ru/vacancy/1234567",
            "50000 - 100000",
            "Требования: опыт работы от 3 лет...",
            "ответственность",
            "Компания",
            "Адрес 4321",
        ),
        Vacancy(
            "Python QT",
            "https://hh.ru/vacancy/7654321",
            "100000 - 150000",
            "Требования: опыт работы от 3 лет...",
            "ответственность",
            "Компания",
            "Адрес 1234",
        )
    ]