# graph = {
#     "0": set(["1", "2"]),
#     "1": set(["0", "3", "4"]),
#     "2": set(["0"]),
#     "3": set(["1"]),
#     "4": set(["2", "3"]),
# }

graph = {
    "0": {"1", "2", "3"},
    "1": {"0", "2"},
    "2": {"0", "1", "4"},
    "3": {"0"},
    "4": {"2"},
}

# print("Graph:", graph)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


dfs(graph, "0")
