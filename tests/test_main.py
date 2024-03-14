from main import return_list_transactions
from main import returns_executed_transactions
from main import returns_list_last_transactions
import json

with open('operations.json', 'rt', encoding='utf-8') as file:
    list_transaction = json.load(file)


def test_return_list_transactions():
    assert return_list_transactions != None


def test_returns_executed_transactions():
    data = list_transaction
    # for transaction in data:
    assert len(returns_executed_transactions(data)) == 85


def test_returns_list_last_transactions():
    data = returns_executed_transactions(list_transaction)
    assert len(returns_list_last_transactions(data)) == 5
