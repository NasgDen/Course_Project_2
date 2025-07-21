import re


class Vacancy:
    """ Класс для работы с вакансиями """
    name: str  # наименование вакансии
    url: str  # ссылка на вакансию
    salary: str  # зарплата
    requirement: str  # требования
    responsibility: str  # ответственность
    company: str  # организация
    address: str  # адрес организации
    __slots__ = (
        "name",
        "url",
        "salary",
        "requirement",
        "responsibility",
        "company",
        "address",
    )

    def __init__(
        self, name, url, salary, requirement, responsibility, company, address
    ):
        self.name = name
        self.url = self.url_validate(url)
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.company = company
        self.address = address

    def __str__(self):
        return f"""Наименование :{self.name}
Ссылка на вакансию: {self.url}
Диапазон зарплат: {self.salary}
Требования: {self.requirement}
Обязанности: {self.responsibility}
Компания: {self.company}
Адрес: {self.address} """

    def __lt__(self, other) -> bool:
        """Метод сравнения атрибута класса 'зарплата'"""
        if isinstance(other, Vacancy):
            salary_first = self.salary.split(" - ")
            salary_second = other.salary.split(" - ")
            avg_salary_first = sum(map(int, salary_first)) / len(salary_first)
            avg_salary_second = sum(map(int, salary_second)) / len(salary_second)
            print(avg_salary_first)
            print(avg_salary_second)
            return avg_salary_first < avg_salary_second
        else:
            raise TypeError("Неверный тип данных")

    @classmethod
    def cast_to_object_list(cls, vacancies) -> list:
        """Метод создает список вакансий"""
        vacancies_list = []
        for vacancy in vacancies.get("items"):
            name = vacancy.get("name")
            url = vacancy.get("alternate_url")
            if vacancy.get("salary") is not None:
                if vacancy.get("salary").get("from") is not None:
                    salary_from = vacancy.get("salary").get("from")
                else:
                    salary_from = "0"
                if vacancy.get("salary").get("to") is not None:
                    salary_to = vacancy.get("salary").get("to")
                else:
                    salary_to = "0"
                salary = f"{salary_from} - {salary_to}"
            else:
                salary = "0 - 0"
            if vacancy.get("snippet").get("requirement") is not None:
                requirement = vacancy.get("snippet").get("requirement")
            else:
                requirement = ""
            if vacancy.get("snippet").get("responsibility") is not None:
                responsibility = vacancy.get("snippet").get("responsibility")
            else:
                responsibility = ""
            company = vacancy.get("employer").get("name")
            if vacancy.get("address") is not None:
                address = f"{vacancy.get("address").get("raw")}"
            else:
                address = ""
            vacancies_list.append(
                cls(name, url, salary, requirement, responsibility, company, address)
            )
        return vacancies_list

    @staticmethod
    def url_validate(url):
        """Валидация url ссылка на вакансию"""
        pattern = r"https://hh.ru/vacancy/\d+"
        if re.match(pattern, url) is None:
            print(f"Неправильная ссылка на ваканси: {url}")
            return ""
        else:
            return url
