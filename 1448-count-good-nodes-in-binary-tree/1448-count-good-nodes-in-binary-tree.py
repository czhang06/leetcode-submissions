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
            msf = max(node.val, msf)
            explore(node.left, msf)
            explore(node.right, msf)
        
        explore(root, float('-inf'))
        return result