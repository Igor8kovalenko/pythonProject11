import os.path

import pytest

from src.functions import read_json


# os.path.join(C:\Users\Dell-PC\PycharmProjects\pythonProject11\tests\conftest.py,'test_operations.json')

def test_read_json(path_to_test_json, expected_result_for_read_json_test):
    assert read_json(path_to_test_json) == expected_result_for_read_json_test


# def test_sort_data():
#     assert sort_data(data_for_sort) == []
