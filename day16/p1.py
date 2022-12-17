import re

graph = {}
node_values = {}

with open("in.txt", "r") as f:
    for line in f:
        line = re.sub('\n|,|;', '', line).split()
        node_label = line[1]
        graph[node_label] = set()
        node_values[node_label] = int(line[4].split("=")[1])
        for neighbour in line[9:]:
            graph[node_label].add(neighbour)

calculated_paths = {}

def dict_vals_to_str(dict):
    string = ''
    for value in dict.values():
        string += str(value)
    return string

visisted = {}

def dfs(node, time, node_values, last):
    if time <= 1: return 0

    node_values_copy = node_values.copy()
    function_key = (node, time, dict_vals_to_str(node_values))

    if function_key in calculated_paths:
        return calculated_paths[function_key]

    # Skip valve
    best_steam = 0
    for neighbour in graph[node]:
        best_steam = max(best_steam, dfs(neighbour, time - 1, node_values_copy, node))

    # Open valve
    steam_val = (time - 1) * node_values_copy[node]
    if not steam_val == 0:
        node_values_copy[node] = 0
        best_steam = max(best_steam, dfs(node, time - 1, node_values_copy, node) + steam_val)

    calculated_paths[function_key] = best_steam

    return best_steam


print(dfs('AA', 30, node_values, 'AA'))



























