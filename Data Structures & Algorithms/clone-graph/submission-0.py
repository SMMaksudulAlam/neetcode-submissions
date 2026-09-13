"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}

        def dfs(nde):
            if(not nde):
                return None
            if(nde.val in nodes):
                return nodes[nde.val]
            
            node = Node(nde.val)
            nodes[nde.val] = node
            neighbors = []
            for neigh in nde.neighbors:
                neighbors.append(dfs(neigh))
            
            node.neighbors = neighbors
            return node
        
        return dfs(node)

