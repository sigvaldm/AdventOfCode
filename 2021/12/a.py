import numpy as np
from copy import deepcopy

class Graph(dict):
    '''Dictionary where you can look up where to go next'''

    def add_edge(self, a, b):

        if a not in self:
            self[a] = []
        self[a].append(b)

        if b not in self:
            self[b] = []
        self[b].append(a)

def traverse(graph, path=["start"]):
    '''Recursive depth-first search'''

    if path[-1]=='end':
        return [path]

    neighbors = graph[path[-1]]
    neighbors = list(filter(lambda a: a.isupper() or a not in path, neighbors))

    paths = []
    for n in neighbors:
        new_path = traverse(graph, path+[n])
        paths += new_path

    return paths

graph = Graph()

with open('input') as file:
    for line in file:
        edge = line.split('\n')[0].split('-')
        graph.add_edge(*edge)

paths = traverse(graph)
print(len(paths))
