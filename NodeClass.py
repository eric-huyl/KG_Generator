from Logger import *
import json

class BasicNode:
    name = ''
    def __init__(self, n):
        self.name = str(n)
        print_info('Creating basic node:' + self.name + '\n')
    def saveToJSON(self, json_file_name):
        node_json = json.dumps(self.__dict__)
        with open(json_file_name, 'w') as f:
            f.write(node_json)

class DieseaseNode(BasicNode):
    description = []
    def __init__(self, n, d):
        BasicNode.__init__(self, n)
        self.description.append(str(d))

    def saveToJSON(self, json_file_name):
        BasicNode.saveToJSON(self, json_file_name)
    def print_self(self):
        for des in self.description:
            print_info(des)


class SymptomNode(BasicNode):
    description = []
    def __init__(self, n, d):
        BasicNode.__init__(self, n)
        self.description.append(str(d))

if __name__ == '__main__':
    node = DieseaseNode('yes', 'Ohhhh')
    node.saveToJSON('yes.json')


