# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        result = None
        n = 0
        def explore(node):
            nonlocal result
            nonlocal n
            if not node:
                return 
            explore(node.left)
            n += 1
            if n == k:
                result = node.val
            
            explore(node.right)
        explore(root)
        return result