import json
from datetime import datetime


def download_operation(filename):
    """
    загружает файл из operations.json
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def transfer_status(list_statuses):
    """
    Фильтр по статусу перевода выполнено
    """
    filter_list = []
    for operations in list_statuses:
        if "state" in operations and operations["state"] == "EXECUTED":
            filter_list.append(operations)
    return filter_list


def sorting_list_date(list_operations,number_operations):
    """
    Сортировка по дате
    """
    list_operations = sorted(list_operations, key=lambda x: x["date"], reverse=True)
    return list_operations[:number_operations]


def all_operation(operation):
    """
    Вывод списка выполненых клиентом операций
    """
    date = datetime.strptime(operation["date"],"%Y-%m-%dT%H:%M:%S/%f").strftime("%d.%m.%Y")
    discript = operation["description"]
    to = operation["to"]
    to = to.replace(to[to.index(" ")+1:-4], "**")
    oper_amount = operation["operationAmount"]["amount"]
    oper_name = operation["operationAmount"]["currency"]["name"]
    if "from" in operation:
        where = operation["from"]
        where = where.replace(where[where.rfind(" ")+7:-4], "** **** ")
        where = where[:where.find(" ") + 5] + ' ' + where[where.find(" ") + 5:]
        return f'{date} {discript}\n{where} -> {to}\n{oper_amount} {oper_name}'
    return f'{date} {discript}\n{to}\n{oper_amount} {oper_name}'