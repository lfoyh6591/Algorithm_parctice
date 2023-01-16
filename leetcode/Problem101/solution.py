# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric2(self, root1, root2):
        if (not root1) and (not root2):
            return True
        
        if (not root1) and root2:
            return False
        if (not root2) and root1:
            return False

        if root1.val != root2.val:
            return False
        
        return self.isSymmetric2(root1.left, root2.right) and self.isSymmetric2(root1.right, root2.left)


    def isSymmetric(self, root: list[TreeNode]) -> bool:
        return self.isSymmetric2(root.left, root.right)