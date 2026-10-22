# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        result = False

        def explore(node, subtree):
            nonlocal result
            if not node:
                return
            if node.val == subtree.val:
                if compare(node, subtree):
                    result = True
            explore(node.left, subtree)
            explore(node.right, subtree)
        def compare(t1, t2):
            if not t1 and not t2:
                return True
            if (not t1) != (not t2):
                return False
            if t1.val != t2.val:
                return False
            return compare(t1.left, t2.left) and compare(t1.right, t2.right)
        explore(root, subRoot)
        return result