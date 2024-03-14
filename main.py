import json
from datetime import datetime


def return_list_transactions():
    """Функция возвращает данные из Json формата"""
    with open('operations.json', 'rt', encoding='utf-8') as file:
        return json.load(file)


def returns_executed_transactions(list_transactions):
    """Функция возвращает список всех операций со статусом'EXECUTED' и исключает некорректные данные по транзакциям"""
    executed_list = []
    for transaction in list_transactions:
        if len(transaction) == 0:
            continue
        else:
            if transaction['state'] == 'EXECUTED':
                executed_list.append(transaction)

    return executed_list


def returns_list_last_transactions(executed_list):
    """Функция возвращает 5 последних,по времени, транзакций """
    for transaction in executed_list:
        new_date = datetime.fromisoformat(transaction['date'])
        transaction['date'] = new_date
    sorted_list = sorted(executed_list, key=lambda x: x['date'], reverse=True)
    return sorted_list[0:5]


list_transactions = return_list_transactions()
executed_list = returns_executed_transactions(list_transactions)
finaly_list = returns_list_last_transactions(executed_list)

for transaction in finaly_list:

    if transaction['description'] == 'Открытие вклада':
        print(
            f"""{transaction['date'].day}.{transaction['date'].month}.{transaction['date'].year} {transaction['description']} **{transaction['to'][-4:]}
на сумму {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']} \n""")

    else:
        if len(transaction['from'].split()) == 2:
            print(
                f"""{transaction['date'].day}.{transaction['date'].month}.{transaction['date'].year} {transaction['description']}
c {transaction['from'].split()[0]} {transaction['from'].split()[1][0:5]} {transaction['from'].split()[1][5:7]}** **** {transaction['from'].split()[1][-4:]} -> {transaction['to'].split()[0]} **{transaction['to'].split()[1][-4:]}
на сумму {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']} \n""")

        elif len(transaction['from'].split()) == 3:
            print(
                f"""{transaction['date'].day}.{transaction['date'].month}.{transaction['date'].year} {transaction['description']}
c {transaction['from'].split()[0]} {transaction['from'].split()[1]} {transaction['from'].split()[2][0:5]} {transaction['from'].split()[2][5:7]}** **** {transaction['from'].split()[2][-4:]} -> {transaction['to'].split()[0]} **{transaction['to'].split()[1][-4:]}
на сумму {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']} \n""")
