# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_node(self, root, p, lists):
        if not root:
            return []
        if root == p:
            return lists + [root]

        l = self.find_node(root.left, p, lists+[root])
        if not l:
            return self.find_node(root.right, p, lists+[root])
        else:
            return l

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        st = self.find_node(root, p, [])
        while st:
            cur = st.pop()
            ret = self.find_node(cur, q, [])
            if ret:
                return cur