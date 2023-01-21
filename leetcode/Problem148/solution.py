# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: list[ListNode]) -> list[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        back = slow.next
        slow.next = None

        head = self.sortList(head)
        back = self.sortList(back)

        root = ListNode()
        root_cur = root
        while head and back:
            if head.val <= back.val:
                root_cur.next = head
                head = head.next
            else:
                root_cur.next = back
                back = back.next
            root_cur = root_cur.next
        
        if head:
            root_cur.next = head
        else:
            root_cur.next = back

        return root.next