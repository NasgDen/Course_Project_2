from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies("Python")

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)


    # for i in range(30):
    #     print(f"{vacancies_list[i].salary}        {i}")


    # Пример работы контструктора класса с одной вакансией
    vacancy = Vacancy(
        "Python Developer",
        "https://hh.ru/vacancy/123456",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет...",
        "ответственность",
        "Компания",
        "Адрес",
    )


if __name__ == "__main__":
    main()
