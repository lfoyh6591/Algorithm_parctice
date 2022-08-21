# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addrecursion(self, n1, n2):
        if n1.next == None:
            return ListNode(n1.val + n2.val, None)
        else:
            ret = ListNode(n1.val + n2.val, self.addrecursion(n1.next, n2.next))
            ret.val += ret.next.val // 10
            ret.next.val %= 10
            return ret
        
    def addTwoNumbers(self, l1, l2):
        temp1 = l1
        temp2 = l2
        len1 = 0
        len2 = 0
        
        while temp1 != None:
            temp1 = temp1.next
            len1 += 1
        
        while temp2 != None:
            temp2 = temp2.next
            len2 += 1
            
        for i in range(0, len1-len2):
            l2 = ListNode(0, l2)
            
        for i in range(0, len2-len1):
            l1 = ListNode(0, l1)

        ret = self.addrecursion(l1, l2)
        
        if ret.val == 0:
            if ret.next == None:
                return ret
            return ret.next
        elif ret.val >= 10:
            carry = ret.val // 10
            ret = ListNode(carry, ret)
            ret.next.val %= 10
            return ret
        else:
            return ret
        