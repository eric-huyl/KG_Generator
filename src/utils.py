import json
import numpy as np


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


def read_from_json(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


class NpEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


def save_to_json(input, output_file):
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(input,
                  json_file,
                  ensure_ascii=False,
                  indent=4,
                  cls=NpEncoder)


def append_to_json(input, output_file):
    with open(output_file, "a", encoding="utf-8") as json_file:
        json.dump(input,
                  json_file,
                  ensure_ascii=False,
                  indent=4,
                  cls=NpEncoder)
