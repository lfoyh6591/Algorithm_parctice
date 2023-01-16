# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        head = ListNode(0, None)
        cur = head

        while (list1 != None) or (list2 != None):
            if list1 == None:
                cur.next = list2
                return head.next
            elif list2 == None:
                cur.next = list1
                return head.next

            if list1.val <= list2.val:
                cur.next = list1
                while list1 and (list1.val <= list2.val):
                    list1 = list1.next
                    cur = cur.next
            elif list2.val <= list1.val:
                cur.next = list2
                while list2 and (list2.val <= list1.val):
                    list2 = list2.next
                    cur = cur.next
        
        return head.next