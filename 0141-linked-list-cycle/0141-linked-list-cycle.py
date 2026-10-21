# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False
        slow, fast = head.next, head.next.next 

        while slow and fast:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return False
        