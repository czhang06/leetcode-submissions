# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = None
        def explore(node, t1, t2):
            nonlocal result
            result = node
            if t1.val < node.val and t2.val < node.val:
                explore(node.left, t1, t2)
            elif t1.val > node.val and t2.val > node.val:
                explore(node.right, t1, t2)
        
        explore(root, p, q)
        return result
            
