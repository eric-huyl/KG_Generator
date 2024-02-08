import json


def print_info(info) -> None:
    print('\033[32m' + str(info) + '\033[0m')


def print_exception(e) -> None:
    print('\033[31m' + str(e) + '\033[0m')


def save_object(object, json_file_name) -> None:
    object_json = json.dumps(object.__dict__)
    with open(json_file_name, 'w') as f:
        f.write(object_json)
        print_info(object + ' saved at ' + json_file_name)


def append_list(item, json_file_name) -> None:
    with open(json_file_name, 'r') as f:
        try:
            list = json.load(f)
        except Exception as e:
            print_exception(e)
            list = []
    with open(json_file_name, 'w') as f:
        list.append(item)
        json.dump(list, f)
