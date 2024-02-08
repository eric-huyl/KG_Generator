import utils
RESPATH = '/resources'
EDGEPATH = '/resources/edges.json'


class Node:
    def __init__(self, attr) -> None:
        self.alias = None
        self.attribute = attr

    def __str__(self) -> str:
        return 'alias: %s attribute: %s' % (self.alias, self.attribute)

    def save(self) -> None:
        json_file_name = RESPATH + '/' + self.attribute + '_'
        + self.alias + '.json'
        utils.save_object(self, json_file_name)


class Edge:
    def __init__(self, attr) -> None:
        self.attribute = attr
        self.src = None
        self.dest = None
        self.condition = []
