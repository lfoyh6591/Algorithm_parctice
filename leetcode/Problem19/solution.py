# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rec(self, head):
        if head:
            self.rec(head.next)
            print(head.val)
            if self.num == 0:
                if head.next:
                    head.next = head.next.next
            self.num -= 1
            return head.next
        else:
            return None

    def removeNthFromEnd(self, head: list[ListNode], n: int) -> list[ListNode]:
        self.num = n
        return self.rec(ListNode(0,head))