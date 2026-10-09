# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def mergeSort(node):
            if not node or not node.next:
                return node

            slow = node
            fast = node

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            temp = slow.next
            slow.next = None

            left = mergeSort(node)
            right = mergeSort(temp)

            dummy = ListNode(0)
            t = dummy

            while left and right:
                if left.val < right.val:
                    t.next = left
                    left = left.next
                else:
                    t.next = right
                    right = right.next

                t = t.next

            if left:
                t.next = left
            else:
                t.next = right

            return dummy.next

        return mergeSort(head)