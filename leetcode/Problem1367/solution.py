# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def find_root_bfs(root, n):
    root_list = []
    if root == None:
        return root_list
    
    q = []
    q.append(root)
    
    while len(q) != 0:
        temp = q.pop(0)
        if temp == None:
            continue
            
        if temp.val == n:
            root_list.append(temp)
    
        q.append(temp.left)
        q.append(temp.right)
        
    return root_list

def dfs(root, head):
    if head == None:
        return True
    
    if root == None:
        return False
    
    if root.val != head.val:
        return False
    
    return (dfs(root.left, head.next) | dfs(root.right, head.next))
        


class Solution:
    def isSubPath(self, head, root) -> bool:
        root_list = find_root_bfs(root, head.val)

        while len(root_list) != 0:
            root = root_list.pop(0)
            if dfs(root, head) == True:
                return True
            
        return False