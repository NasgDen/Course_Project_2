class Vacancy:
    name: str # наименование вакансии
    url: str # ссылка на вакансию
    salary: str # зарплата
    company: str # организация
    address: str # адрес организации

    def __ini__(self, name, url, salary, company, address):
        self.name = name
        self.url = url
        self.salary = salary
        self.company = company
        self.address = address

    @staticmethod
    def cast_to_object_list(vacancies):
        return vacancies.get("items")