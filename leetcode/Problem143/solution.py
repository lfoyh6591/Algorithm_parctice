# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def lenList(self, head):
        if head == None:
            return 0
        
        ret = 0
        while head != None:
            ret += 1
            head = head.next
            
        return ret
            
    def reverseList(self, head):
        if head == None:
            return None
        
        l = []
        while head != None:
            temp = head.next
            head.next = None
            l.append(head)
            head = temp
        
        head = ListNode(0, l[-1])
        temp = head.next
        for i in range(len(l)-1, -1, -1):
            temp.next = l[i]
            temp = temp.next
        
        return head.next
    
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head2 = head
        l = []
        while head2 != None:
            temp = head2.next
            head2.next = None
            l.append(head2)
            head2 = temp
        
        
            
        middle = (len(l)-1)//2
        front = l[:middle+1]
        end = l[middle+1:]
        end.reverse()
        end.append(None)

        root = ListNode(0, head)
        for i in range(0, middle+1):
            head.next = front[i]
            head = head.next
            head.next = end[i]
            head = head.next
            
        head = root.next
                
        