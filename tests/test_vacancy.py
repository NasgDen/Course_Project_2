from src.vacancy import Vacancy

def test_init_vacation(new_vacation):
    assert new_vacation.name == "Python Developer"
    assert new_vacation.url == "https://hh.ru/vacancy/1234567"
    assert new_vacation.salary == "100000 - 150000"
    assert new_vacation.requirement == "Требования: опыт работы от 3 лет..."
    assert new_vacation.responsibility == "ответственность"
    assert new_vacation.company == "Компания"
    assert new_vacation.address == "Адрес"


def test_lt_vacation(list_vacation):
    assert list_vacation[0] > list_vacation[1]

