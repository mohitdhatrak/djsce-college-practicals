def print_matrix(matrix):
    for row in matrix:
        print(row)

# example 1 - image in readme
# flow = [[0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0]] 

# capacity = [[0, 7, 2, 4, 0], 
#             [0, 0, 0, 8, 10],
#             [0, 0, 0, 1, 0],
#             [0, 0, 0, 0, 5],
#             [0, 0, 0, 0, 0]]

# print("Initial capacity matrix:")
# print_matrix(capacity)

# residual capacity = capacity - flow (initially flow = 0 so this is same as capacity)
# residual_capacity = [[0, 7, 2, 4, 0], 
#                      [0, 0, 0, 8, 10],
#                      [0, 0, 0, 1, 0],
#                      [0, 0, 0, 0, 5],
#                      [0, 0, 0, 0, 0]]

# example 2 - https://iq.opengenus.org/maximum-flow-problem-overview
flow = [[0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]] 

capacity = [[0, 8, 10, 0, 0, 0], 
            [0, 0, 0, 2, 7, 0],
            [0, 3, 0, 0, 12, 0],
            [0, 0, 0, 0, 0, 10],
            [0, 0, 0, 4, 0, 8], 
            [0, 0, 0, 0, 0, 0]]

print("Initial capacity matrix:")
print_matrix(capacity)

residual_capacity = [[0, 8, 10, 0, 0, 0], 
                     [0, 0, 0, 2, 7, 0],
                     [0, 3, 0, 0, 12, 0],
                     [0, 0, 0, 0, 0, 10],
                     [0, 0, 0, 4, 0, 8], 
                     [0, 0, 0, 0, 0, 0]]

num_of_nodes = len(capacity)
max_flow = 0

# source = 'S'
# sink = 'T'

# node_to_index = {
#     'S': 0,
#     'A': 1,
#     'B': 2,
#     'C': 3,
#     'T': 4
# }

source = '1'
sink = '6'

node_to_index = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5
}

index_to_node = {v: k for k, v in node_to_index.items()} # or simply type the reverse of above object

def possible_paths(current_path, all_paths):
    current_source = node_to_index[current_path[-1]]
    for i in range(0, num_of_nodes):
        if capacity[current_source][i] != 0:
            path = current_path.copy()
            path.append(index_to_node[i])
            all_paths.append(path)

def get_all_paths():
    all_paths = []

    possible_paths([source], all_paths) # initially to get all single path links from source, then use each to get all possible paths

    current_path = all_paths[0]
    index = 0

    while current_path != all_paths[-1]: # till last element of all paths array is not reached
        if current_path[-1] != sink: # if last node of path is not sink, then path is incomplete, fetch possible paths
            possible_paths(current_path, all_paths)
            all_paths.remove(current_path)
        else:
            index += 1
        
        current_path = all_paths[index]

    return all_paths

possible_paths = get_all_paths()
print("\nPossible paths:", possible_paths)

# now, for all possible paths, 
# select one path, check bottleneck capacity, if more than 0, add that as an augmenting path
# update the residual capacity and flow matrices

for path in possible_paths:
    # first we find the bottleneck capacity of the path
    bottleneck = 1000 # any large value initially
    for i in range(0, len(path) - 1):
        from_node = node_to_index[path[i]]
        to_node = node_to_index[path[i + 1]]

        if residual_capacity[from_node][to_node] < bottleneck: # we find the min value and set it as bottleneck
            bottleneck = residual_capacity[from_node][to_node]
    
    if bottleneck > 0: # this means path can be considered
        str = ""
        for node in path:
            str += node + (' -> ' if node != path[-1] else '')
        print("\nConsider augmenting path:", str)
        print("Bottleneck capacity:", bottleneck)

        max_flow += bottleneck

        for i in range(0, len(path) - 1):
            from_node = node_to_index[path[i]]
            to_node = node_to_index[path[i + 1]]

            residual_capacity[from_node][to_node] -= bottleneck
            flow[from_node][to_node] = bottleneck
        
        print("Current flow matrix:")
        print_matrix(flow)
        print("Current residual capacity matrix:")
        print_matrix(residual_capacity)

print("\nMax flow in network:", max_flow)