import requests


def get_vacancies(name: str):
    """Поиск и получение данных с api.hh.ru/vacancies"""
    url = "https://api.hh.ru/vacancies"
    params = {"text": name, "period": 3}
    vacancies = requests.get(url, params)
    return vacancies.json()
