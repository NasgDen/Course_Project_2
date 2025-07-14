class Vacancy:
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
        self.url = url
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.company = company
        self.address = address

    @classmethod
    def cast_to_object_list(cls, vacancies):
        vacancies_list = []
        for vacancy in vacancies.get("items"):
            name = vacancy.get("name")
            url = vacancy.get("alternate_url")
            if vacancy.get("salary") is not None:
                if vacancy.get("salary").get("from") is not None:
                    salary_from = vacancy.get("salary").get("from")
                else:
                    salary_from = ""
                if vacancy.get("salary").get("to") is not None:
                    salary_to = vacancy.get("salary").get("to")
                else:
                    salary_to = ""
                salary = f"{salary_from} - {salary_to}"
            else:
                salary = 0
            requirement = vacancy.get("snippet").get("requirement")
            responsibility = vacancy.get("snippet").get("responsibility")
            company = vacancy.get("employer").get("name")
            if vacancy.get("address") is not None:
                address = f"{vacancy.get("address").get("raw")}"
            else:
                address = ""
            vacancies_list.append(
                cls(name, url, salary, requirement, responsibility, company, address)
            )
        return vacancies_list
