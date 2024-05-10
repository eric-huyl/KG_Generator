import os
from src.entity_recognition import entity_recog

InputParagraphFolder = 'temp/input/'
OutputEntitiesFolder = 'temp/entities/'


def recog_entities() -> list:
    global InputParagraphFolder
    global OutputEntitiesFolder
    for root, file in find_all_files(InputParagraphFolder):
        recog_file_name = file.split('.txt')[0] + '.json'
        input_path = os.path.join(root, file)
        output_path = os.path.join(OutputEntitiesFolder, recog_file_name)
        entity_recog(input_path, output_path)


def find_all_files(base):
    for root, dirs, files in os.walk(base):
        for f in files:
            yield root, f


if __name__ == '__main__':
    recog_entities()
