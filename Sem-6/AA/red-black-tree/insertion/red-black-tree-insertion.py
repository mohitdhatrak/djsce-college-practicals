import copy


class node:
    def __init__(self, value, left, right, parent, colour):
        self.value = value
        self.colour = colour
        self.left = left
        self.right = right
        self.parent = parent

def change_colour(colour):
    if colour == 'B':
        return 'R'
    else:
        return 'B'

def recolour_nodes(current_parent):
    print("Action: recolour")
    global root_node

    if current_parent.parent != root_node:
        current_parent.parent.colour = change_colour(current_parent.parent.colour)
    
    current_parent.parent.left.colour = change_colour(current_parent.parent.left.colour)
    current_parent.parent.right.colour = change_colour(current_parent.parent.right.colour)

def rotate_and_recolour_nodes(child, parent, grandparent, case):
    print("Action: rotate + recolour")
    global root_node

    # simple logic is to sort the 3 nodes in order
    nodes = [child, parent, grandparent]
    sorted_nodes = sorted(nodes, key=lambda node: node.value)

    # middle node becomes new parent and the others become its child nodes
    new_parent = copy.deepcopy(sorted_nodes[1])
    new_left_child = copy.deepcopy(sorted_nodes[0])
    new_right_child = copy.deepcopy(sorted_nodes[2])
    
    # update each node's left, right and parent nodes
    new_parent.parent = grandparent.parent
    new_parent.left = new_left_child
    new_parent.right = new_right_child
    new_left_child.parent = new_parent
    new_right_child.parent = new_parent

    if case == 'special':
        # child_to_move = None
        if parent.left != new_left_child and parent.left != new_right_child:
            child_to_move = parent.left
            new_left_child.right = child_to_move
        else:
            child_to_move = parent.right
            new_right_child.left = child_to_move
    else:
        new_left_child.left = None
        new_left_child.right = None
        new_right_child.left = None
        new_right_child.right = None

    # recolouring follows this logic
    new_parent.colour = 'B'
    new_left_child.colour = 'R'
    new_right_child.colour = 'R'

    # updating the position of nodes in the tree
    if grandparent.parent == None: # or case == 'special' 
        root_node = new_parent
    else:
        if grandparent.parent.left == grandparent:
            grandparent.parent.left = new_parent
        else:
            grandparent.parent.right = new_parent

def check_conflict(node, node_parent, case):
    if node_parent.colour == 'R':
        if case != 'special':
            print("\nR-R conflict!")
        if node_parent.parent.left == None or node_parent.parent.right == None:
            rotate_and_recolour_nodes(node, node_parent, node_parent.parent, case)
        elif node_parent.parent.left.colour != node_parent.parent.right.colour:
            rotate_and_recolour_nodes(node, node_parent, node_parent.parent, case)
        else:
            recolour_nodes(node_parent)
        return True
    else:
        print("\nNo conflict!")
        return False

def check_whole_tree(node):
    if node is None:
        return None

    if node.colour == 'R':
        if node.left is not None and node.left.colour == 'R': 
            return node.left
        elif node.right is not None and node.right.colour == 'R':
            return node.right

    left_child = check_whole_tree(node.left)
    right_child = check_whole_tree(node.right)

    if left_child:
        return left_child
    elif right_child:
        return right_child
    else:
        return None   

def insert_node(value):
    global root_node
    current_parent = root_node
    current_value = value
    parent_found = False
    
    while not parent_found: # traverse to get the parent node for current value, then insert
        if current_value < current_parent.value:
            if current_parent.left is None:
                new_node = node(current_value, None, None, current_parent, 'R')
                current_parent.left = new_node # inserted new node
                parent_found = True

                # after insertion, handle R-R conflict if any
                is_conflict = check_conflict(new_node, current_parent, 'normal')

                # check for any new R-R conflicts in whole tree
                if is_conflict:
                    conflict_node = check_whole_tree(root_node)
                    if conflict_node is not None:
                        print("\nNEW R-R conflict")
                        check_conflict(conflict_node, conflict_node.parent, 'special')
            else:
                current_parent = current_parent.left
        else:
            if current_parent.right is None:
                new_node = node(current_value, None, None, current_parent, 'R')
                current_parent.right = new_node # inserted new node 
                parent_found = True

                # after insertion, handle R-R conflict if any
                is_conflict = check_conflict(new_node, current_parent, 'normal')

                # check for any new R-R conflicts in whole tree
                if is_conflict:
                    conflict_node = check_whole_tree(root_node)
                    if conflict_node is not None:
                        print("NEW R-R conflict")
                        check_conflict(conflict_node, conflict_node.parent, 'special')
            else:
                current_parent = current_parent.right 

    return root_node
                
def print_tree(node, indent=0, prefix="root"):
    if indent == 0:
        print()
    if node is not None:
        print(f"{'' if indent == 0 else '|' * indent}" + "--" * indent + f"{'' if indent == 0 else ' '}" + f"{prefix}: {node.value} {node.colour}")
        print_tree(node.left, indent + 1, "left")
        print_tree(node.right, indent + 1, "right")

# RUN - to get full tree
# input_values = [13, 21, 10, 18, 19, 33, 28, 43, 63, 5, 4, 74]
# root_node = node(input_values[0], None, None, None, 'B')
# for i in range(1, len(input_values)):
#     root_node = insert_node(input_values[i])
# print_tree(root_node)

# RUN - to get tree for each insertion
root_node = node(None, None, None, None, None)
input_values = []
while True:
    print("Action Menu:")
    print("1. Insert node and print tree")
    print("2. Stop")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = int(input("Enter node value: "))
        input_values.append(value)
        
        if len(input_values) == 1:
            root_node = node(value, None, None, None, 'B')
        else:
            root_node = insert_node(value)
        print_tree(root_node)
        print()
    elif choice == 2:
        print("Node insertion complete")
        break

    else:
        print("Invalid input!\n")