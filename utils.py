import json


def print_info(info) -> None:
    print('\033[32m' + str(info) + '\033[0m')


def print_exception(e) -> None:
    print('\033[31m' + str(e) + '\033[0m')


def append_list(item, json_file_name) -> None:
    list = []
    list.extend(json_file_name)
    with open(json_file_name, 'w') as f:
        list.append(item)
        json.dump(list, f)


def find_list(item, json_file_name) -> bool:
    with open(json_file_name, 'r') as f:
        try:
            list = json.load(f)
            if item in list:
                return True
        except Exception as e:
            print_exception(e)
    return False
