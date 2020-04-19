class Solution:
    def invertTree(self, root):
        if not root:
            return None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        elif not (root.left or root.right):
            return root
        root.right, root.left = (root.left, root.right)
        return root