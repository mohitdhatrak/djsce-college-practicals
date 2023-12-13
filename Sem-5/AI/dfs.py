def dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)
        if source == goal_state:
            path.append("(GOAL)")
            return path

        # leaf node, backtrack
        if source not in graph:
            return path

        for neighbour in graph[source]:
            path = dfs(graph, neighbour, path)
            # to stop at goal node
            # if "GOAL" in path:
            #     break

    return path


# graph = {
#     "A": ["B", "C", "D"],
#     "B": ["E"],
#     "C": ["F", "G"],
#     "D": ["H"],
#     "E": ["I"],
#     "F": ["J"],
# }

graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
goal_state = "8"

print("Following is the Depth-First Search: ")
path = dfs(graph, "5")

print(" ".join(path))

if "(GOAL)" in path:
    print("Goal state found")
else:
    print("Goal state not found")
