import json


def download_operation(filename):
    """
    загружает файл из operations.json
    """
    with open(filename, 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


# def executed_transactions(data):
#     new_item = []
#     for item in data:
#         if item.get('state') == 'EXECUTED':
#             new_item.append(item)
#
#     new_item.sort(key=lambda x: x.get('data'), reverse=True)
#     return new_item

def sorting_by_date_of_banking_transactions(operations):
    """
    Сортировка по дате
    """
    operation_data = sorted(operations, key=lambda x: x.get('date', ""), reverse=True)
    return operation_data


def completed_operations(data, score):
    """
    Выполненные операции (EXECUTED)
    :return: 
    """
    count = 0
    new_data = []
    for datas in data:
        if datas['state'].lower == 'EXECUTED'.lower():
            new_data.append(datas)
            count += 1
            if count == score:
                return new_data
                break
