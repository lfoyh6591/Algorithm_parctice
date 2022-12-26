# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head == None:
            return head
        root = ListNode(0, head)
        length = 0
        while head != None:
            length += 1
            head = head.next
            
        rotatenum = k % length
                
        head = root.next
        for i in range(0, length - rotatenum - 1):
            head = head.next
            
        temp = head.next
        head.next = None
        last = root.next
        root.next = temp
        
        head = root.next
        
        if head == None:
            return last
        
        while head.next != None:
            head = head.next
            
        head.next = last
        
        return root.next