class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges)!=n-1):
            return False

        graph = {i: set() for i in range(n)}
        for (u, v) in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        def dfs(nde, p):
            if(nde in visited):
                return False
            visited.add(nde)
            neigh = graph[nde]
            for n in neigh:
                if(n==p):
                    continue
                if(not dfs(n, nde)):
                    return False
            return True
        
        acyc = dfs(0, -1)
        if(not acyc):
            return False
        if(len(visited) == n):
            return True
        return False