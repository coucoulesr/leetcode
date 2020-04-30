# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.max_path_sum = float('-inf')
        self.pathSum(root)
        return self.max_path_sum
        
    def pathSum(self, node):
        if node == None:
            return 0
        left = max(0, self.pathSum(node.left))
        right = max(0, self.pathSum(node.right))
        self.max_path_sum = max(self.max_path_sum, left + right + node.val)
        return max(left, right) + node.val