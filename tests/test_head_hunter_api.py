from src.head_hunter_api import HeadHunterAPI
from unittest.mock import patch


@patch('requests.get')
def test_api_connection(mock_get):
    mock_get.return_value.json.return_value = {"name: name"}
    mock_get.return_value.status_code = 200
    pass

