# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: list[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        q = [root]
        ret = []
        state = True
        while q:
            l = []
            new_q = []
            while q:
                node = q.pop(0)
                l.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            
            q = new_q
            if state:
                ret.append(l)
            else:
                ret.append(l[::-1])
            state = not state

        return ret