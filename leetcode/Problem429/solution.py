"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if root == None:
            return []
        
        num_child = [1]
        q = []
        q.append(root)
        res = []
        level = 0
        
        while len(q) != 0:
            present_level = []
            num = 0
            for i in range(num_child[level]):
                temp = q.pop(0)
                present_level.append(temp.val)
                for child in temp.children:
                    if child == None:
                        continue
                    num += 1
                    q.append(child)
            
            res.append(present_level)
            num_child.append(num)
            level += 1
            
        return res
            