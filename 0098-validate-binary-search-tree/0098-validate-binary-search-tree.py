# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def explore(node, low, hi):
            if not node:
                return True
            if node.val <= low or node.val >= hi:
                return False
            return explore(node.left, low, node.val) and explore(node.right, node.val, hi)
        
        return explore(root, -float('inf'), float('inf'))