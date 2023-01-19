# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> list[TreeNode]:
        if not preorder:
            return None

        val = preorder[0]
        idx = inorder.index(val)

        return TreeNode(val, self.buildTree(preorder[1:1+idx], inorder[:idx]), self.buildTree(preorder[1+idx:], inorder[idx+1:]))