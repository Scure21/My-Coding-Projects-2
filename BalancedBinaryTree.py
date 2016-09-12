class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
        
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        
    def get_value(self):
        return self.value
        
        
def superbalancedTree(root):
    '''
    O(n) time and O(n) space, the depths list never gets bigger than 2 but the nodes stack takes 0(n)
    '''
    depths = [] # we short-circuit as soon as we find more than 2

    # we'll treat this list as a stack that will store tuples of (node, depth)
    nodes_stack = [(root, 0)]
    #nodes_stack.append(()

    while len(nodes_stack):

        # pop a node and its depth from the top of our stack
        node, depth = nodes_stack.pop()

        # case: we found a leaf
        if (not node.left) and (not node.right):

            # we only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if (len(depths) > 2) or \
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False

        # case: this isn't a leaf - keep stepping down
        else:
            if node.left:
                nodes_stack.append((node.left, depth + 1))
            if node.right:
                nodes_stack.append((node.right, depth + 1))

    return True
            