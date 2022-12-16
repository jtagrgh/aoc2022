import re
from queue import PriorityQueue

class node:
    def __init__(self, name = "", value = 0):
        self.name = name
        self.value = value
    def __eq__(self, another):
        if another == self.name:
            return True
        elif hasattr(another, 'name') and self.name == another.name:
            return True
        else:
            return False
    def __hash__(self):
        return hash(self.name)
    def __repr__(self):
        return self.name

graph = {}

with open("in.txt", "r") as f:
    for line in f:
        line = re.sub('\n|,|;', '', line).split()
        new_node = node(line[1], int(line[4].split("=")[1]))
        graph[new_node] = set()
        for neighbour in line[9:]:
            graph[new_node].add(neighbour)

def greed(graph, path, time_left, current_depth):
    root = path[-1]
    best_distances = {key: 0 if key==root else float('inf') for key in graph.keys()}
    priority_queue = PriorityQueue()
    unvisited_nodes = set(key.name for key in graph.keys())
    priority_queue.put((0, 'AA'))

    while(len(unvisited_nodes) > 0):
        this_node = priority_queue.get()
        this_node_key = this_node[1]
        if this_node_key not in unvisited_nodes:
            continue
        this_node_distance = this_node[0]
        best_distances[this_node_key] = this_node_distance
        for neighbour in graph[this_node_key]:
            if neighbour in unvisited_nodes:
                priority_queue.put((this_node_distance + 1, neighbour))

        unvisited_nodes.remove(this_node_key)

    print(best_distances)

greed(graph, ['AA'], 0, 1)









