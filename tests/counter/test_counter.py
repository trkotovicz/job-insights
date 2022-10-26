import json
from unittest.mock import mock_open, patch

from src.counter import count_ocurrences


def test_counter():
    mock_text = {
        "ocurrences": """This mock is here just to test the counter function.
        So, I'm gonna throw some random words here:
        python, Python, PYthON, pythoN,
        javascript, Javascript, JavaScript, JAVASCRIPT"""
    }

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_text))):
        assert count_ocurrences("arquivo.json", "python") == 4
        assert count_ocurrences("arquivo.json", "javascript") == 4
