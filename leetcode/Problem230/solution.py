# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def cal_length(self, root):
        if not root:
            return 0
        return self.cal_length(root.left) + 1 + self.cal_length(root.right)

    def kthSmallest(self, root: list[TreeNode], k: int) -> int:
        left = self.cal_length(root.left)
        if k-1 == left:
            return root.val

        if k-1 > left:
            return self.kthSmallest(root.right, k-left-1)
        else:
            return self.kthSmallest(root.left, k)