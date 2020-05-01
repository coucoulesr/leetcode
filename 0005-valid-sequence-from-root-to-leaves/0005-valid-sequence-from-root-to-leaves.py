# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root, arr):
        if not root or (root.val and not arr):
            return False
        if root.val == arr[0]:
            if len(arr) == 1:
                if not root.left and not root.right:
                    return True
                else:
                    return False
            return self.isValidSequence(root.left, arr[1::]) or self.isValidSequence(root.right, arr[1::])
        else:
            return False