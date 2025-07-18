from src.vacancy import Vacancy


response = {"items":
                  [{"name": "name",
                   "alternate_url": "https://hh.ru/vacancy/122842251",
                   "salary":
                       {
                           "from": "10",
                           "to": "50"
                       },
                   "snippet":
                       {
                            "requirement": "requirement",
                            "responsibility": "responsibility"
                       },
                   "employer":
                       {
                           "name": "name"
                       },
                   "address":
                       {
                           "raw": "raw"
                       }
                   }]
    }
result = [Vacancy(
        "name",
        "https://hh.ru/vacancy/122842251",
        "10 - 50",
        "requirement",
        "responsibility",
        "name",
        "raw",
    )]
result1 = [Vacancy(
        "name",
        "https://hh.ru/vacancy/122842251",
        "10 - 50",
        "requirement",
        "responsibility",
        "name",
        "raw",
    )]

aa = Vacancy.cast_to_object_list(response)
print(aa[0].name)
print(result)
print(result1)