graph = {
    "A": {"B": 9, "C": 4, "D": 7},
    "B": {"E": 11},
    "C": {"E": 17, "F": 12},
    "D": {"F": 14},
    "E": {"Z": 5},
    "F": {"Z": 9},
}

# Define the heuristic values for A* search - h(n) for each node
heuristic = {"A": 21, "B": 14, "C": 18, "D": 18, "E": 5, "F": 8, "Z": 0}
start_node = input("Enter Start Node: ")  # this is also start node at the beginning
curr_node = start_node
goal_node = input("Enter Goal Node: ")


# this function returns f(n) value, formula -> f(n) = g(n) + h(n)
def costFormula(path, node):  # path <- path of previous node , node <- current node
    # h(n) - heuristic value of current node
    h = heuristic[node]

    # g(n) - sum of path values till current node
    g = 0

    # gets sum of all path, except last node to current node -> ADD this separately
    # reason - as i + 1 won't be defined if we go till last node
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]
        g += graph[from_node][to_node]

    # adding last path separately
    from_node = path[-1]
    to_node = node
    g += graph[from_node][to_node]

    return g + h


open_list = []  # has a list for each node - [node, node heuristic value, node path]
close_list = []  # has all nodes that have been visited

# add start node to open list
open_list.append([start_node, heuristic[start_node], [start_node]])

try:
    while True:
        # since we sort the list, we keep getting newer nodes to explore
        parent_node = open_list[0][0]
        current_path = open_list[0][2]

        close_list.append(parent_node)  # once we visit we add it to close list

        if parent_node == goal_node:  # breaking condition
            break

        print(f"\nCurrently at node: {parent_node}")
        # once we select a parent node, we explore all its options and add to open list
        for j in graph[parent_node]:
            open_list.append([j, costFormula(current_path, j), current_path + [j]])
            # sort the open list to solve for smaller f(n) values first
            open_list = sorted(open_list, key=lambda x: x[1])

        # remove the current parent node from open list, only if it is 1st after sorting
        #  i.e. if it has the lowest f(n) value
        if open_list[0][0] == parent_node:
            open_list.remove(open_list[0])  # removes the first list from open list

        print(f"Open List: {open_list}")
        print(f"Closed List: {close_list}")

    print(
        f"\nSo the optimized path from {start_node} to {goal_node} is {open_list[0][2]} and distance is {open_list[0][1]}"
    )
except Exception as e:
    print("\mSomething went wrong, mostly node not found: ", e)
