import json


from src.json_sever import JSONSaver
from unittest.mock import patch


@patch("json.dump")
def test_write_vacancy(mock_get):
    mock_get.return_value.json.return_value.return_value = [{"test": "test"}]
    json_test = JSONSaver("test.json")
    json_test.write_vacancy([])
    assert mock_get.called is True


@patch("json.load")
def test_read_vacancy(mock_get):
    with open("test.json", mode="w", encoding="utf-8") as file:
        json.dump([], file, indent=4, ensure_ascii=False)
    mock_get.return_value.load.return_value = [{"test": "test"}]
    json_test = JSONSaver("test.json")
    json_test.read_vacancy()
    assert mock_get.called is True


@patch("json.load")
def test_delete_vacancy(mock_get, list_vacation):
    with open("test.json", mode="w", encoding="utf-8") as file:
        json.dump([], file, indent=4, ensure_ascii=False)
    mock_get.return_value.load.return_value = [{"name": "name"}]
    mock_get.return_value.convert_object_to_dict.return_value = [{"name": "name"}]
    mock_get.return_value.read_vacancy.return_value = list_vacation
    json_test = JSONSaver("test.json")
    json_test.delete_vacancy(list_vacation)
    assert mock_get.called is True
