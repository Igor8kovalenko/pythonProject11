from coverage import data
from poetry.installation.operations import operation
from src.functions import change_date_format, sort_data, read_json, masking_card, output_data, output_money
import unittest
import pytest
import json
import os
path_operations = os.path.join('..', 'src', 'operations.json')
def test_read_json():

    assert type(read_json(path_operations)) == list

def test_change_date_format():
    assert change_date_format("2018-02-03T07:16:28.366141") == "03.02.2018"


def test_sort_data():
    data = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]
    assert sort_data(data) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                                'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                                'to': 'Счет 64686473678894779589'},
                               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
                                'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},                                'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
                                'to': 'Счет 35383033474447895560'},
                               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                                'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                                'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                                'to': 'Счет 11776614605963066702'}]


def test_masking_card():
    assert masking_card("Счет 90424923579946435907") == "Счет **5907"
    assert masking_card("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
# #

def test_output_money(operation_amount):
    assert (operation_amount.keys('8221.37')) == '8221.37'

# def test_output_data():


if __name__ == '__main__':
    unittest.main()