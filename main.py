from src.api import get_vacancies
from src.utils import write_json_file


def main():
    vacancies = get_vacancies("python")
    write_json_file(vacancies,"data/vacancies.json")



if __name__ == "__main__":
    main()