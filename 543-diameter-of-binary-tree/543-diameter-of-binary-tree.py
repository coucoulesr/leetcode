class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        height_left = self.height(root.left)
        diameter_left = self.diameterOfBinaryTree(root.left)
        height_right = self.height(root.right)
        diameter_right = self.diameterOfBinaryTree(root.right)
        return max(height_left + height_right, max(diameter_left, diameter_right))
        
    def height(self, tree):
        if not tree:
            return 0
        return 1 + max(self.height(tree.left), self.height(tree.right))