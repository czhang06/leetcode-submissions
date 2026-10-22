# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result = []

        def explore(node, depth):
            nonlocal result
            if not node:
                return
                
            if depth > len(result):
                result.append(node.val)
            explore(node.right, depth + 1)
            explore(node.left, depth + 1)

        explore(root, 1)
        return result
