class uf:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.count = 1
    
    def find(self):
        nde = self
        while(nde != nde.parent):
            nde = nde.parent
        
        cur = self
        while(cur != nde):
            temp = cur.parent
            cur.parent = nde
            cur = temp
        return nde
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #dfs
        """
        graph = {}
        for (u, v) in edges:
            if(u not in graph):
                graph[u] = set()
            if(v not in graph):
                graph[v] = set()

            graph[u].add(v)
            graph[v].add(u)


        path = set()
        def dfs(nde, p):
            if(nde in path):
                return
            path.add(nde)
            neigh = graph.get(nde, set())
            for nei in neigh:
                if(nei == p):
                    continue
                dfs(nei, nde)
            return
        count = 0
        for i in range(n):
            if(i not in path):
                count +=1
                dfs(i, -1)

        return count
        """

        nodes = {}
        parents = set()

        for i in range(n):
            node = uf(i)
            nodes[i] = node
            parents.add(i)
        
        for (u, v) in edges:
            node_u = nodes[u]
            node_v = nodes[v]

            pr_u = node_u.find()
            pr_v = node_v.find()

            if(pr_u != pr_v):
                if(pr_u.count >= pr_v.count):
                    pr_u.count += pr_v.count
                    pr_v.parent = pr_u
                    parents.remove(pr_v.val)
                else:
                    pr_v.count += pr_u.count
                    pr_u.parent = pr_v
                    parents.remove(pr_u.val)

        return len(parents)        

        


            