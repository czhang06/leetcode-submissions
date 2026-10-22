# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        result = 0
        def explore(node, depth):
            nonlocal result
            if not node:
                return
            if not node.left and not node.right:
                result = max(result, depth)
                return
            explore(node.left, depth + 1)
            explore(node.right, depth + 1)
        
        explore(root, 1)
        return result
        