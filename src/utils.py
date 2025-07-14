import json


def write_json_file(data, file_name: str) -> None:
    """Запись данных в файл формата json"""
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
