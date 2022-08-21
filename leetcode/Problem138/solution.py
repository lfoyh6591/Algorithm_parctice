
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        node_list = []
        node_dic = {}
        index = 0
        temp = head
        while head != None:
            node_dic[head.next] = index
            index += 1
            head = head.next
        
        while temp != None:
            if temp.random == None:
                random = -1
            else :
                random = node_dic[temp.random.next]
                
            node_list.append((Node(temp.val), random))
            temp = temp.next
            
        node_list.append((None, 0))
            
        for index, (node, random) in enumerate(node_list):
            if node != None:
                node.next = node_list[index+1][0]
                node.random = node_list[random][0]
            
        return node_list[0][0]