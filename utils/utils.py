import json


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




