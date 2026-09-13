class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for (u, v) in edges:
            if(u not in graph):
                graph[u] = set()
            if(v not in graph):
                graph[v] = set()
            graph[u].add(v)
            graph[v].add(u)

        cycle_edge = set()
        visited = {}
        rank = 1

        def dfs(nde, p):
            nonlocal rank
            if(nde in visited):
                return False, visited[nde]
            visited[nde] = rank 
            rank+=1
            neigh = graph[nde]
            my_rank = visited[nde]
            acyc = True
            for n in neigh:
                if(n==p):
                    continue
                acyc_, rank = dfs(n, nde)
                acyc = acyc and acyc_
                if(not acyc_ and rank<=my_rank):
                    cycle_edge.add((nde, n))
                my_rank = min(my_rank, rank)
            return acyc, my_rank

        dfs(1, -1)
        #print(cycle_edge)
        for i in range(len(edges)-1, -1, -1):
            (u, v) = edges[i]
            if((u, v) in cycle_edge or (v, u) in cycle_edge):
                return edges[i]
        return []
        