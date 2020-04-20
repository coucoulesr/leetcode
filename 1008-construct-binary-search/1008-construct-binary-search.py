# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        # Special case: input is empty list
        if not preorder:            
            return None
    
        # Preorder condition: first value in input must be root
        root = TreeNode(preorder[0])
        
        # Special case: input size 1 (preorder[1::] not safe)
        if len(preorder) == 1:
            return root

        # Call recursive addNode function which adds a node from the root
        for value in preorder[1::]:
            self.addNode(root, value)

        return root
        
    def addNode(self, root, value):
        # If value to add is bigger than root, go right
        if value > root.val:
            # If there is no right child, value becomes right child
            if not root.right:
                root.right = TreeNode(value)
            # If there is a right child, recurse on right child
            else:
                self.addNode(root.right, value)
        # If value is smaller, go left
        else:
            # If there is no left child, value becomes left child
            if not root.left:
                root.left = TreeNode(value)
            # If there is a left child, recurse on left child
            else:
                self.addNode(root.left, value)