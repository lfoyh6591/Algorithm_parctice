# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root) -> list[int]:
        if not root:
            return []
        st = []
        ret = []
        while root:
            st.append(root)
            root = root.left
        while st:
            print(st)
            cur = st.pop()
            ret.append(cur.val)
            if cur.right:
                cur = cur.right
                while cur:
                    st.append(cur)
                    cur = cur.left

        return ret