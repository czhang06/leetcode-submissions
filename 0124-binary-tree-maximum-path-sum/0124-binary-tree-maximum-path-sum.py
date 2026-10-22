# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        result = float('-inf')
        
        def dfs(node):
            nonlocal result
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            result = max(result, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return result