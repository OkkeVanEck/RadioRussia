class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid
        self.neighbours = []

    def add_neighbour(self, node):
        self.neighbours.append(node)