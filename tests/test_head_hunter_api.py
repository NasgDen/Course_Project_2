from unittest.mock import patch

from src.head_hunter_api import HeadHunterAPI


@patch("requests.get")
def test_api_connection_code_fault(mock_get):
    mock_get.return_value.json.return_value = {"test: test"}
    mock_get.return_value.status_code = 300
    hh_test = HeadHunterAPI()
    hh_test._HeadHunterAPI__api_connect("test")
    assert mock_get.called is True


@patch("requests.get")
def test_api_connection_code_200(mock_get):
    mock_get.return_value.json.return_value = {"test: test"}
    mock_get.return_value.status_code = 200
    hh_test = HeadHunterAPI()
    hh_test._HeadHunterAPI__api_connect("test")
    assert mock_get.called is True
