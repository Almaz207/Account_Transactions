from main import return_list_transactions
from main import returns_executed_transactions
from main import returns_list_last_transactions

def test_return_list_transactions():
    data = return_list_transactions()
    assert len(return_list_transactions()) == 101

def test_returns_executed_transactions(selection_list):
    assert returns_executed_transactions


def test_returns_list_last_transactions(list_transactions):
    returns_list_last_transactions()
    assert len list_last_transactions()







