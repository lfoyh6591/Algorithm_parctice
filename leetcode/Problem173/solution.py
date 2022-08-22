# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root):
        self.st = []
        self.pushleftall(root)
        
    def next(self) -> int:
        node = self.st.pop()
        self.pushleftall(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.st) > 0

    def pushleftall(self, root) :
        while root != None:
            self.st.append(root)
            root = root.left
        
    
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()