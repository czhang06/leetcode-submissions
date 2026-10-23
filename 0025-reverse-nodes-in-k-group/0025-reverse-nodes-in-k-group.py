# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            first = group_prev.next
            group_prev.next = kth
            group_prev = first
            