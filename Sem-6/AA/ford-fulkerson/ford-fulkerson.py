def print_matrix(matrix):
    for row in matrix:
        print(row)

flow = [[0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]] 

capacity = [[0, 7, 2, 4, 0], 
            [0, 0, 0, 8, 10],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0]]

print("Initial capacity matrix:")
print_matrix(capacity)

# residual capacity = capacity - flow (initially flow = 0 so this is same as capacity)
residual_capacity = [[0, 7, 2, 4, 0], 
                     [0, 0, 0, 8, 10],
                     [0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 5],
                     [0, 0, 0, 0, 0]]

num_of_nodes = 5
source = 'S'
sink = 'T'
max_flow = 0

node_to_index = {
    'S': 0,
    'A': 1,
    'B': 2,
    'C': 3,
    'T': 4
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

    while current_path != all_paths[-1]: # till last element of path is not 
        if current_path[-1] != sink:
            possible_paths(current_path, all_paths)
            all_paths.remove(current_path)
            index = 0
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

        if residual_capacity[from_node][to_node] < bottleneck:
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