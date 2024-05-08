from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import split_sentence


def entity_recog(input_array) -> None:
    ner_pipeline = pipeline(
        Tasks.named_entity_recognition,
        "damo/nlp_raner_named-entity-recognition_chinese-base-cmeee",
    )
    result = ner_pipeline(input_array)
    split_sentence.save_to_json(result, 'recognized_entities.json')


if __name__ == "__main__":
    input = split_sentence.read_from_json("sentences.json")
    entity_recog(input)
