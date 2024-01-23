import json
import datetime

def download_operation(filename):
    """загружает файл из operations.json
    """
    with open(filename, 'r', encoding='utf-8') as file:
        operations = json.load(file)