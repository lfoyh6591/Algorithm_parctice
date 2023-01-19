# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def makelist(self, root):
        if not root:
            return []
        
        return self.makelist(root.left) + [root.val] + self.makelist(root.right)

    def isValidBST(self, root: list[TreeNode]) -> bool:
        l = self.makelist(root)
        for i in range(len(l)-1):
            if l[i+1] <= l[i]:
                return False

        return True