"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None
        
        d = {}
        copy = Node(node.val)
        d[node.val] = copy
        q = [node]
        while q:
            n = q.pop()
            new = d[n.val]
            for nd in n.neighbors:
                if nd.val not in d:
                    d[nd.val] = Node(nd.val)
                    q.append(nd)
                new.neighbors.append(d[nd.val])
        
        return d[node.val]
