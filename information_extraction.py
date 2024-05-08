import split_sentence


def simplify_entity(file_path):
    content = split_sentence.read_from_json(file_path)
    for sentence in content:
        print(sentence['output'])


if __name__ == '__main__':
    simplify_entity('recognized_entities.json')
