from src.head_hunter_api import HeadHunterAPI
from src.json_sever import JSONSaver
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
    # json_saver.write_vacancy("data/vacancy.json", vacancies_list)



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

    # Добавление вакансии в файл формата JSON
    # json_saver.add_vacancy("data/vacancy.json", vacancy)

    # Удаление вакансий из файла формата JSON
    json_saver.delete_vacancy("data/vacancy.json", vacancy)

if __name__ == "__main__":
    main()
