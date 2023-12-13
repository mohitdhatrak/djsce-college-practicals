visited = []
queue = []


def bfs(visited, graph, node, goal_state):
    goal_found = False
    visited.append(node)
    queue.append(node)

    # Creating loop to visit each node
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m == goal_state:
            print("(GOAL)", end=" ")
            goal_found = True
            # to stop at goal state
            # break

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return goal_found


graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}

print("Following is the Breadth-First Search: ")
goal_found = bfs(visited, graph, "5", "8")

if goal_found:
    print("\nGoal state found")
else:
    print("\nGoal state not found")
