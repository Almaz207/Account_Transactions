from main import return_list_transactions
from main import returns_executed_transactions
from main import returns_list_last_transactions
import json

with open('operations.json', 'rt', encoding='utf-8') as file:
    list_transactions = json.load(file)


def test_returns_executed_transactions():
    data = list_transactions
    assert len(list(filter(returns_executed_transactions, data))) == 100


def test_returns_list_last_transactions():
    data= returns_executed_transactions(list_transactions)
    assert len(list(filter(returns_executed_transactions,data))) == 5
