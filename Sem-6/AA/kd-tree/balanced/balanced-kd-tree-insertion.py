class node:
    def __init__(self, value, left, right, parent, compare):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.compare = compare
        
def toggle_compare(variable):
    if variable == 0:
        return 1
    else:
        return 0  
    
def insert_node(value, direction):
    global root_node
    current_parent = root_node
    current_value = value
    parent_found = False
  
    if direction == "left" and current_parent.left is not None:
        current_parent = root_node.left
    elif direction == "right" and current_parent.right is not None:
        current_parent = root_node.right

    current_compare = current_parent.compare

    while not parent_found: # traverse to get the parent node for current value, then insert
        if current_value[current_compare] <= current_parent.value[current_compare]:
            if current_parent.left is None:
                new_node = node(current_value, None, None, current_parent, toggle_compare(current_compare))
                current_parent.left = new_node # inserted new node
                parent_found = True
            else:
                current_parent = current_parent.left
                current_compare = toggle_compare(current_compare)
        else:
            if current_parent.right is None:
                new_node = node(current_value, None, None, current_parent, toggle_compare(current_compare))
                current_parent.right = new_node # inserted new node 
                parent_found = True
            else:
                current_parent = current_parent.right   
                current_compare = toggle_compare(current_compare)

    return root_node

def print_tree(node, indent=0, prefix="root"):
    if indent == 0:
        print()
    if node is not None:
        print(f"{'' if indent == 0 else '|' * indent}" + "--" * indent + f"{'' if indent == 0 else ' '}" + f"{prefix}: ({node.value[0]}, {node.value[1]})")
        print_tree(node.left, indent + 1, "left")
        print_tree(node.right, indent + 1, "right")

# RUN - to get full tree
input_values = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
sorted_input = sorted(input_values, key=lambda x: x[0]) # initial sort as per 'x'
print("Round 0 (sorted by x): ")
print("Sorted ndoes:", sorted_input)
midpoint = int(len(sorted_input) / 2) if len(sorted_input) % 2 != 0 else int(len(sorted_input) / 2) - 1 # left biased (if 2 midpoints, we take left one), so we used ternary operator
root_node = node(sorted_input[midpoint], None, None, None, 0)
left = []
right = []
for i in range(0, midpoint):
    left.append(sorted_input[i])
for i in range(midpoint + 1, len(sorted_input)):
    right.append(sorted_input[i])
# compare 0 -> means x
# compare 1 -> means y
current_compare = 1
round = 1
while len(left) != 0 and len(right) != 0:
    print(f"\nRound {round} (sorted by {'x' if round % 2 == 0 else 'y'}):")
    if len(left) != 0:
        left = sorted(left, key=lambda x: x[current_compare])
        print("Left nodes:", left)
        left_mid = int(len(left) / 2) if len(left) % 2 != 0 else int(len(left) / 2) - 1 
        insert_node(left[left_mid], "left")
        left.remove(left[left_mid])
    if len(right) != 0:
        right = sorted(right, key=lambda x: x[current_compare])
        print("Right nodes:", right)
        right_mid = int(len(right) / 2) if len(right) % 2 != 0 else int(len(right) / 2) - 1 
        insert_node(right[right_mid], "right")
        right.remove(right[right_mid])
    current_compare = toggle_compare(current_compare)
    round += 1

print_tree(root_node)