class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for (u, v) in edges:
            if(u not in graph):
                graph[u] = set()
            if(v not in graph):
                graph[v] = set()

            graph[u].add(v)
            graph[v].add(u)


        #dfs
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
            