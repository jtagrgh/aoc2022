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

def dfs(node, time, node_values):
    if time <= 1: return 0, node_values

    node_values_copy = node_values.copy()
    function_key = (node, time, dict_vals_to_str(node_values))

    if function_key in calculated_paths:
        return calculated_paths[function_key]

    # Skip valve
    best_steam = 0
    best_node_vals = node_values
    for neighbour in graph[node]:
        ret_steam, ret_node_vals = dfs(neighbour, time - 1, node_values_copy)
        if ret_steam > best_steam:
            best_steam = ret_steam
            best_node_vals = ret_node_vals

    # Open valve
    steam_val = (time - 1) * node_values_copy[node]
    if not steam_val == 0:
        node_values_copy[node] = 0
        ret_steam, ret_node_vals = dfs(node, time - 1, node_values_copy)
        ret_steam += steam_val
        if ret_steam > best_steam:
            best_steam = ret_steam
            best_node_vals = ret_node_vals

    calculated_paths[function_key] = (best_steam, best_node_vals)

    return best_steam, best_node_vals

person_results = dfs('AA', 26, node_values)
elephant_results = dfs('AA', 26, person_results[1])

print(person_results[0] + elephant_results[0])

























