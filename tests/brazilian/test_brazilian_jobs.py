# import json
# from unittest.mock import mock_open, patch
from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    # mock_dict = {
    #     "titulo": "Maquinista", "salario": "2000", "tipo": "trainee"
    # }
    # mock_translated = {
    #     "title": "Maquinista", "salary": "2000", "type": "trainee"
    # }

    # with patch("builtins.open", mock_open(read_data=json.dumps(mock_dict))):
    # given = read_brazilian_file('arquivo.json')
    # assert given == mock_translated

    given = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for row in given:
        assert "title" in row
        assert "salary" in row
        assert "type" in row
