# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: list[TreeNode]) -> bool:
        if (not root.left) and (not root.right):
            return True
        if (not root.left) and root.right:
            return False
        if (not root.right) and root.left:
            return False

        st = [root.left, root.right]

        while st:
            r = st.pop()
            l = st.pop()

            if (not r) and (not l):
                continue
            if (not r) and l:
                return False
            if (not l) and r:
                return False
            if l.val != r.val:
                return False

            st.append(l.left)
            st.append(r.right)
            st.append(r.left)
            st.append(l.right)

        return True