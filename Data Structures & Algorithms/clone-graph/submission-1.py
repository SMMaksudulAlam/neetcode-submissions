"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dic = {}
        def build(nde):
            if(not nde):
                return None
            if(nde.val in dic):
                return dic[nde.val]
            node = Node(nde.val)
            dic[node.val] = node
            neigh = nde.neighbors
            for nei in neigh:
                node.neighbors.append(build(nei))
            return node
        return build(node)