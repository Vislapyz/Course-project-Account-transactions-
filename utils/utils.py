import json


def download_operation(filename):
    """загружает файл из operations.json
       дата из файла
    """
    with open(filename, 'r', encoding='utf-8') as file:
        operations = json.load(file)

    operation_data = sorted(operations, key=lambda x: x.get('date', ""), reverse=True)
    return operation_data
