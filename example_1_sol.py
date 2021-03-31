import unittest
from unittest.mock import patch
from typing import Dict
import requests
import time


def sleeping():
    time.sleep(5)


def fetch_data(url: str) -> Dict:

    r = requests.get(url)

    sleeping()

    if isinstance(r, FakeResponse):
        print(r)

    if r.status_code != 200:
        return {}

    return {"text": r.text}


# print(fetch_data("http://www.google.com"))


class FakeResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text


class TestFetch(unittest.TestCase):

    @patch("requests.get")
    def test_fetch_data_happy(self, mock_get):
        mock_get.return_value = FakeResponse(status_code=200, text="hello")

        expected_data = {"text": "hello"}

        actual_data = fetch_data(url="http://www.google.com")

        self.assertEqual(expected_data, actual_data)

    @patch("example_1_sol.sleeping")
    @patch("requests.get")
    def test_fetch_data_sad(self, mock_get, mock_sleeping):
        mock_get.return_value = FakeResponse(status_code=404, text="")

        expected_data = {}

        actual_data = fetch_data(url="http://www.google.com")

        self.assertEqual(expected_data, actual_data)


if __name__ == '__main__':
    unittest.main()
