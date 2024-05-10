import split_sentence


def simplify_entity(file_path):
    edges = []
    content = split_sentence.read_from_json(file_path)
    for sentence in content:
        entity_edge = []
        for entity in sentence['output']:
            reduced_entity = [entity['type'], entity['span']]
            entity_edge.append(reduced_entity)
        edges.append(entity_edge)
    return edges


if __name__ == '__main__':
    split_sentence.save_to_json(simplify_entity('recognized_entities.json'),
                                'raw_edges.json')
