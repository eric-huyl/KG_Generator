import json
import utils
RESPATH = 'D:/KG_GENERATOR/res'


def save_graph(graph=[], path='') -> None:
    graph_json = json.dumps(graph)
    with open(path, 'w') as f:
        f.write(graph_json)


def load_graph(path='') -> []:
    with open(path, 'r') as f:
        graph = json.load(f)
    return graph


def backward_search(sym='', graph_path='') -> []:
    dieseases = []
    graph = load_graph(graph_path)
    for edge in graph:
        try:
            if edge['symptom'] == sym and edge['relation'] == 'dis_cause_sym':
                dieseases.append(edge['diesease'])
            if edge['symptom'] == sym and edge['relation'] == 'sym_cause_sym':
                dieseases.extend(backward_search(sym, graph_path))
        except Exception as e:
            utils.print_exception(e)
            continue
    return dieseases

def forward_reason(dis='', cond=[], graph_path='') -> []:
    graph = load_graph(graph_path)
    for edge in graph:
        try:
            if edge['diesease'] == dis and 


if __name__ == '__main__':
    backward_search('a', 'test.json')
