import json
import numpy as np


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


def split_sentences_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().replace("\n", "")
            sentences = content.split("。")  # 使用句号分隔句子
    except FileNotFoundError:
        print("文件不存在或无法读取。")
    sentences.pop()
    if sentences:
        for sentence in sentences:
            sentence.strip()
    else:
        print("空句子。")
    append_to_json(sentences, "sentences.json")


def read_from_json(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


if __name__ == "__main__":
    file_path = "input.txt"  # 替换为实际的文件路径
    result = split_sentences_from_file(file_path)
