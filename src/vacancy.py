class Vacancy:
    name: str # наименование вакансии
    url: str # ссылка на вакансию
    salary: str # зарплата
    requirement: str # требования
    company: str # организация
    address: str # адрес организации

    def __init__(self, name, url, salary, requirement, company, address):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement
        self.company = company
        self.address = address

    @staticmethod
    def cast_to_object_list(vacancies):
        return vacancies.get("items")