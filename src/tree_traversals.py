class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            # the value must go right    
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)

#Pre Order
def print_tree_pre_order(root):
    print(root.value)

    if root.left:
        print_tree_pre_order(root.left)

    if root.right:
        print_tree_pre_order(root.right)

# In Order
def print_tree_in_order(root):
    if root.left:
        print_tree_in_order(root.left)

    if root.right:
        print_tree_in_order(root.right)


# Post Order
def print_tree_post_order(root):
    if root.left:
        print_tree_post_order(root.left)

    if root.right:
        print_tree_post_order(root.right)





# Basic setup of tree traversals 
# setup 
# loop until items are gone
# pop
# your own code, go nuts 
# add next nodes 

def breadth_first_traversal(root):
    # create a queue
    queue = []
     # add the first item to the queue
    queue.append(root)    

    # process items in the queue
    while len(queue) > 0:
        # dequeue an item
        node = queue.pop(0)

        # evaluate the node
        print(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



def depth_first_traversal(root):
    # create a stack
    stack = []
    # add the first item to the stack
    stack.append(root)    

    # process items in the queue
    while len(stack) > 0:
        # dequeue an item
        node = stack.pop()

        # evaluate the node
        print(node.value)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)



def in_order_array(root):
    my_array = []
    def generate_in_order_array(root):
        if root.left:
            generate_in_order_array(root.left)

        my_array.append(root.value)

        if root.right:
            generate_in_order_array(root.right)

    generate_in_order_array(root)
    return my_array



root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)


my_array = in_order_array(root)
print(my_array)