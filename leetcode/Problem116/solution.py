
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return None

        q = [root]
        while q:
            new_q = []
            next_node = None
            while q:
                now = q.pop()
                now.next = next_node
                next_node = now
                if now.right:
                    new_q.append(now.right)
                if now.left:
                    new_q.append(now.left)

            q = new_q[::-1]
        
        return root