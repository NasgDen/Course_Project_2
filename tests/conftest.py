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
        "Адрес",
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