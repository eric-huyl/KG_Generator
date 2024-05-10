from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from . import utils


def entity_recog(input_path, output_path) -> None:
    try:
        with open(input_path, "r", encoding="utf-8") as file:
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
    edges = []
    ner_pipeline = pipeline(
        Tasks.named_entity_recognition,
        "damo/nlp_raner_named-entity-recognition_chinese-base-cmeee",
        device='cuda'
    )
    result = ner_pipeline(sentences)
    for sentence in result:
        entity_edge = []
        for entity in sentence['output']:
            reduced_entity = [entity['type'], entity['span']]
            entity_edge.append(reduced_entity)
        edges.append(entity_edge)
    utils.save_to_json(edges, output_path)