# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> list[ListNode]:
        temp = headA
        la = 0
        while temp:
            la += 1
            temp = temp.next
        temp = headB
        lb = 0
        while temp:
            lb += 1
            temp = temp.next

        if la > lb:
            for i in range(la-lb):
                headA = headA.next
        elif lb > la:
            for i in range(lb-la):
                headB = headB.next

        for i in range(min(la, lb)):
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next

        return None