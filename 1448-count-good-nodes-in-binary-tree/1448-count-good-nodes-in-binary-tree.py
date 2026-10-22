# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def explore(node, msf):
            nonlocal result
            if not node:
                return
            if node.val >= msf:
                result += 1
            explore(node.left, max(node.val, msf))
            explore(node.right, max(node.val, msf))
        
        explore(root, -1 * 10**4 - 1)
        return result