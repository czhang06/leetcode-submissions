# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        result = ListNode(0) #dummy
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        c1 = head
        c2 = slow.next

        slow.next = None

        prev = None
        curr = c2

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        c2 = prev
        curr = result
        while c1 and c2:
            curr.next = c1
            c1 = c1.next
            curr = curr.next
            curr.next = c2
            c2 = c2.next
            curr = curr.next
        if c1:
            curr.next = c1
        elif c2:
            curr.next = c2
        
        return result.next
