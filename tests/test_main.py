from main import return_list_transactions
from main import returns_executed_transactions
from main import returns_list_last_transactions
import json

with open('operations.json', 'rt', encoding='utf-8') as file:
    list_transactions = json.load(file)

executed_list = returns_executed_transactions(list_transactions)
finaly_list=returns_list_last_transactions(executed_list)


def test_returns_executed_transactions(list_transactions):
    assert len(returns_executed_transactions(list_transactions)) !=0


def test_returns_list_last_transactions(executed_list):
    assert len (returns_executed_transactions(executed_list)) == 5







