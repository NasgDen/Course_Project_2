from src.api import get_vacancies
from src.utils import write_json_file
from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies("Python")
    print(hh_vacancies)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)

    # Пример работы контструктора класса с одной вакансией
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "100 000-150 000 руб.",
                     "Требования: опыт работы от 3 лет...", "Компания", "Адрес")



if __name__ == "__main__":
    main()