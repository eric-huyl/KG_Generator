import json


def print_info(info) -> None:
    print('\033[32m' + str(info) + '\033[0m')


def save_to_json(object, json_file_name) -> None:
    object_json = json.dumps(object.__dict__)
    with open(json_file_name, 'w') as f:
        f.write(object_json)
        print_info(object + ' saved at ' + json_file_name)
