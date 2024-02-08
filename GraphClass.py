import utils
import json


class BasicObject:
    def __init__(self) -> None:
        self.index = None
        self.alais = None
        self.attribute = None

    def __str__(self) -> str:
        return 'index: %s alais: %s' % (self.index, self.alais)

    def save(self, json_file_name) -> None:
        utils.save_to_json(self, json_file_name)


class BasicNode(BasicObject):
    def __init__(self) -> None:
        super().__init__()
        self.description = None
        self.manual = None


class BasicEdge(BasicObject):
    def __init__(self) -> None:
        self.src = None
        self.dest = None

    def __str__(self) -> str:
        return self.src + ' -> ' + self.dest

    def saveToJSON(self, json_file_name):
        node_json = json.dumps(self.__dict__)
        with open(json_file_name, 'w') as f:
            f.write(node_json)