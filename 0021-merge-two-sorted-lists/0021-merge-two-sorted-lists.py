# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        c1 = list1
        c2 = list2
        result = None

        if not c1:
            return c2
        if not c2:
            return c1

        if c1.val < c2.val:
            result = c1
            c1 = c1.next
            
        else:
            result = c2
            c2 = c2.next
            
        curr = result
        while c1 and c2:
            if c1.val < c2.val:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next
        
        if c1:
            curr.next = c1
        else:
            curr.next = c2
        
        return result
        