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
            
paths_array = []
def print_paths(root, path):
    new_path = path + [root.value]

    if not root.left and not root.right:
        paths_array.append(new_path)

    # if you can go left, recurse left
    if root.left: 
        print_paths(root.left, new_path.copy())

    if root.right:
        print_paths(root.right, new_path.copy())

# Reccursion 
# A recursive function is a function defined in terms of itself via self-referential expressions. 
# This means that the function will continue to call itself and repeat its behavior until some 
# condition is met to return a result.

root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)