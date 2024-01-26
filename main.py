from utils.utils import download_operation, transfer_status, sorting_list_date, all_operation

def main(filename, number_operations):
    data = download_operation(filename)
    data = transfer_status(data)
    data = sorting_list_date(data, number_operations)
    for operation in data:
        print(all_operation(operation))
        print()

main("utils/operations.json", 5)
