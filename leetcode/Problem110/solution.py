# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tree_height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    
    return 1+max(tree_height(root.left), tree_height(root.right))

class Solution:
    def isBalanced(self, root) -> bool:
        if root == None:
            return True
            
        if abs(tree_height(root.left) - tree_height(root.right)) > 1:
            return False
        
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False