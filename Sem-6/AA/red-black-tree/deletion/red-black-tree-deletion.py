class node:
    def __init__(self, value, colour, left, right, parent):
        self.value = value
        self.colour = colour
        self.left = left
        self.right = right
        self.parent = parent

def remove_node(node):
    parent = node.parent

    if node == parent.left:
        parent.left = None
    else:
        parent.right = None

def delete_node_case1(node):
    remove_node(node)

    return False # for case 1 no DB node is formed

def delete_node_case2():
    global db_node

    # just remove double black from node
    db_node = node(None, None, None, None, None)

    return False # case 2 removes the DB node from root

def delete_node_case3(sibling_node):
    global db_node

    parent = db_node.parent
    sibling_node.colour = 'R'

    if parent.colour == 'R':
        parent.colour = 'B'
        return False
    else:
        db_node = parent
        return True

def delete_node_case4(sibling_node):
    global db_node
    db_parent = db_node.parent

    # swap colours of parent and sibling of DB node
    sibling_node.colour, db_parent.colour = db_parent.colour, sibling_node.colour

    if db_parent.left == db_node: # this means rotate left to move parent towards DB node
        new_parent = db_parent.right
        temp_node = new_parent.left
        
        new_parent.left = db_parent
        new_parent.parent = db_parent.parent
        db_parent.parent = new_parent
        db_parent.right = temp_node
        # also update the new parent ka parent node -- or else these nodes won't get printed
        new_parent.parent.right = new_parent

    else: # rotate right to move parent towards DB node
        new_parent = db_parent.left
        temp_node = new_parent.right
        
        new_parent.right = db_parent
        new_parent.parent = db_parent.parent
        db_parent.parent = new_parent
        db_parent.left = temp_node
        # also update the new parent ka parent node -- or else these nodes won't get printed
        new_parent.parent.left = new_parent

    return True # DB node still exists

def delete_node_case5(sibling_node, near_nephew):
    # swap colours of sibling node and near nephew of DB node
    sibling_node.colour, near_nephew.colour = near_nephew.colour, sibling_node.colour

    if sibling_node.parent.left == sibling_node: # this means rotate left to move away from DB node
        new_parent = sibling_node.right
        temp_node = new_parent.left
        
        new_parent.left = sibling_node
        new_parent.parent = sibling_node.parent
        sibling_node.parent = new_parent
        sibling_node.right = temp_node
        # also update the new parent ka parent node -- or else these nodes won't get printed
        new_parent.parent.left = new_parent

    else: # rotate right to move away from DB node
        new_parent = sibling_node.left
        temp_node = new_parent.right
        
        new_parent.right = sibling_node
        new_parent.parent = sibling_node.parent
        sibling_node.parent = new_parent
        sibling_node.left = temp_node
        # also update the new parent ka parent node -- or else these nodes won't get printed
        new_parent.parent.right = new_parent

    return delete_node_case6(new_parent, sibling_node) # now new parent is the sibling and sibling node is the far nephew of DB node

def delete_node_case6(sibling_node, far_nephew):
    global db_node
    db_parent = db_node.parent

    # swap colours of sibling node and far nephew of DB node
    db_parent.colour, sibling_node.colour = sibling_node.colour, db_parent.colour

    if db_parent.left == db_node: # this means rotate left to move parent towards DB node
        new_parent = db_parent.right
        temp_node = new_parent.left
        
        new_parent.left = db_parent
        new_parent.parent = db_parent.parent
        db_parent.parent = new_parent
        db_parent.right = temp_node
        # also update the new parent ka parent node -- or else these nodes won't get printed
        new_parent.parent.right = new_parent

    else: # rotate right to move parent towards DB node
        new_parent = db_parent.left
        temp_node = new_parent.right
        
        new_parent.right = db_parent
        new_parent.parent = db_parent.parent
        db_parent.parent = new_parent
        db_parent.left = temp_node
        # also update the new parent ka parent node -- or else these nodes won't get printed
        new_parent.parent.left = new_parent

    far_nephew.colour = 'B'

    db_node = node(None, None, None, None, None)
    return False # remove DB node

def delete_node(value):
    global root_node
    global db_node
    current_parent = root_node
    current_value = value
    node_found = False
    node_to_delete = node(None, None, None, None, None)
    
    while not node_found: # traverse to get the node for current value, then delete
        if current_value == current_parent.value:
            node_to_delete = current_parent
            node_found = True

            # if node to delete is not a leaf node, below process happens
            # swap node value with either smallest element in its right sub-tree (inorder successor) 
            # or largest element in its left sub-tree (inorder predecessor)
            temp_node = node_to_delete
            if node_to_delete.left is not None: # inorder predecessor
                temp_node = node_to_delete.left
                while temp_node.right is not None:
                    temp_node = temp_node.right
            elif node_to_delete.right is not None: # inorder successor
                temp_node = node_to_delete.right
                while temp_node.left is not None:
                    temp_node = temp_node.left

            # swap values of nodes
            temp_node.value, node_to_delete.value = node_to_delete.value, temp_node.value
            # update node to delete
            node_to_delete = temp_node
            db_node = node_to_delete

        elif current_value < current_parent.value:
            current_parent = current_parent.left
        else:
            current_parent = current_parent.right

    db_node_exists = True # every time when we delete a node, we get a DB node, once deletion is complete DB node is gone
    is_node_deleted = False

    while db_node_exists:
        # case 1 - when node is red and leaf
        if node_to_delete.colour == 'R' and node_to_delete.left is None and node_to_delete.right is None:
            db_node_exists = delete_node_case1(node_to_delete)

        # case 2 - when root node is DB node
        elif db_node == root_node:
            db_node_exists = delete_node_case2()
        
        # case 3, 5, 6 - when DB node and it's sibling is black
        elif (db_node.parent.left is None or db_node.parent.left.colour == 'B') and \
                (db_node.parent.right is None or db_node.parent.right.colour == 'B'):
            
            if db_node.parent.left == db_node: # this means DB node is on left, sibling on right
                sibling_node = db_node.parent.right # children of sibling node are called nephew
                        
                # case 3 - when both nephews are black (or don't exist i.e. external leaf node is black)
                if (sibling_node.left is None or sibling_node.left.colour == 'B') and \
                        (sibling_node.right is None or sibling_node.right.colour == 'B'):
                    db_node_exists = delete_node_case3(sibling_node)
                
                # case 5 - when near nephew is red
                elif sibling_node.left.colour == 'R': 
                    db_node_exists = delete_node_case5(sibling_node, sibling_node.left)

                # case 6 - when far nephew is red
                elif sibling_node.right.colour == 'R':
                    db_node_exists = delete_node_case6(sibling_node, sibling_node.right)

            else: # this means DB node is on right, sibling on left
                sibling_node = db_node.parent.left # children of sibling node are called nephew
                
                # case 3 - when both nephews are black (or don't exist i.e. external leaf node is black)
                if (sibling_node.left is None or sibling_node.left.colour == 'B') and \
                        (sibling_node.right is None or sibling_node.right.colour == 'B'):
                    db_node_exists = delete_node_case3(sibling_node)
                
                # case 5 - when near nephew is red
                elif sibling_node.right.colour == 'R': 
                    db_node_exists = delete_node_case5(sibling_node, sibling_node.right)

                # case 6 - when far nephew is red
                elif sibling_node.left.colour == 'R':
                    db_node_exists = delete_node_case6(sibling_node, sibling_node.left)
            
            # we remove the node from tree
            if not is_node_deleted:
                remove_node(node_to_delete)
                is_node_deleted = True
        
        # case 4 - when node sibling is red
        else:
            if db_node.parent.left == db_node: # this means DB node is on left, sibling on right
                sibling_node = db_node.parent.right # children of sibling node are called nephew
                db_node_exists = delete_node_case4(sibling_node)

            else: # this means DB node is on right, sibling on left
                sibling_node = db_node.parent.left # children of sibling node are called nephew     
                db_node_exists = delete_node_case4(sibling_node)

def print_tree(node, indent=0, prefix="root"):
    if indent == 0:
        print()
    if node is not None:
        print("|" * indent + "--" * indent + f"{'' if indent == 0 else ' '}" + f"{prefix}: {node.value} {node.colour}")
        print_tree(node.left, indent + 1, "left")
        print_tree(node.right, indent + 1, "right")

# example 1
# Start - hardcode the sample tree -- covers cases 1 (delete 38), 5 and 6 (delete 30)
db_node = node(None, None, None, None, None)
root_node = node(10, 'B', None, None, None)
n1 = node(5, 'R', None, None, root_node)
n2 = node(30, 'R', None, None, root_node)
n3 = node(2, 'B', None, None, n1)
n4 = node(9, 'B', None, None, n1) 
n5 = node(25, 'B', None, None, n2)
n6 = node(40, 'B', None, None, n2)
n7 = node(38, 'R', None, None, n6)

root_node.left = n1
root_node.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n6.left = n7
# End

# example 2
# Start - hardcode the sample tree -- covers cases 2 and 3 (delete 15)
# db_node = node(None, None, None, None, None)
# root_node = node(10, 'B', None, None, None)
# n1 = node(5, 'B', None, None, root_node)
# n2 = node(20, 'B', None, None, root_node)
# n3 = node(1, 'B', None, None, n1)
# n4 = node(7, 'B', None, None, n1) 
# n5 = node(15, 'B', None, None, n2)
# n6 = node(30, 'B', None, None, n2)

# root_node.left = n1
# root_node.right = n2
# n1.left = n3
# n1.right = n4
# n2.left = n5
# n2.right = n6
# End

# example 3
# Start - hardcode the sample tree -- covers case 4 (delete 15)
# db_node = node(None, None, None, None, None)
# root_node = node(10, 'B', None, None, None)
# n1 = node(5, 'B', None, None, root_node)
# n2 = node(20, 'B', None, None, root_node)
# n3 = node(1, 'B', None, None, n1)
# n4 = node(7, 'B', None, None, n1) 
# n5 = node(15, 'B', None, None, n2)
# n6 = node(30, 'R', None, None, n2)
# n7 = node(25, 'B', None, None, n6)
# n8 = node(40, 'B', None, None, n6)

# root_node.left = n1
# root_node.right = n2
# n1.left = n3
# n1.right = n4
# n2.left = n5
# n2.right = n6
# n6.left = n7
# n6.right = n8
# End

print("Initial tree:")
print_tree(root_node)
print()

while True:
    print("Action Menu:")
    print("1. Delete node and print tree")
    print("2. Stop")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = int(input("Enter node value: "))
        
        delete_node(value)
        print_tree(root_node)

        print()
    elif choice == 2:
        print("Node deletion complete")
        break

    else:
        print("Invalid input!\n")