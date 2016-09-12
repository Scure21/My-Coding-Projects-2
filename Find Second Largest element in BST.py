

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
    #We're doing one walk down our BST, which means O(h)O(h) time,
    #where hh is the height of the tree (again, that's O(\lg{n})O(lgn) 
    #if the tree is balanced, O(n)O(n) otherwise). O(1)O(1) space.
    def largest(self,root_node):
        current = root_node
        while current:
            if not current.right:
                return current.value
            current = current.right
            
    def find_second_largest(self, root_node):
        if not (root_node.left or root_node.right):
            raise Exception('Tree must have at least 2 nodes')
    
        current = root_node
    
        while current:
            # case: current is largest and has a left subtree
            # 2nd largest is the largest in that subtree
            if current.left and not current.right:
                return BinaryTreeNode.largest(self, current.left)
    
            # case: current is parent of largest, and
            # largest has no children, so
            # current is 2nd largest
            if current.right and \
            not current.right.left and \
            not current.right.right:
                return current.value
    
            current = current.right