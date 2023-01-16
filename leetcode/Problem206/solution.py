# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
        st = []
        while head:
            st.append(head)
            head = head.next
        
        head = ListNode(0, None)
        cur = head
        while st:
            temp = st.pop()
            temp.next = None
            cur.next = temp
            cur = cur.next
        
        return head.next