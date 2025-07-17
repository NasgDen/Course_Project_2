from src.head_hunter_api import HeadHunterAPI
from src.json_sever import JSONSaver
from src.utils import (filter_vacancies, get_top_vacancies,
                       get_vacancies_by_salary, print_vacancies,
                       sort_vacancies)
from src.vacancy import Vacancy


def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies("Python")

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Сохранения списка вакансий в файл формата JSON
    json_saver = JSONSaver()
    json_saver.write_vacancy(vacancies_list)

    # Пример работы контструктора класса с одной вакансией
    vacancy = Vacancy(
        "Python Developer",
        "https://h.ru/vacancy/1234567",
        "10000000000-150000 руб.",
        "Требования: опыт работы от 3 лет...",
        "ответственность",
        "Компания",
        "Адрес",
    )

    # Добавление вакансии в файл формата JSON
    json_saver.add_vacancy(vacancy)
    json_saver.add_vacancy(vacancy)

    # Удаление вакансий из файла формата JSON
    # json_saver.delete_vacancy(vacancy)

    # Фильтрация вакансий
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    salary_range = input("Введите диапазон зарплат: ").replace(" ", "").split("-")
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # Сортировка вакансий
    sorted_vacancies = sort_vacancies(ranged_vacancies)

    # Вывод top список вакансий
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод информации о вакансиях в консоль
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
