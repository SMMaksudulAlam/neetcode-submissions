import heapq as hq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for (u, v, t) in times:
            if(u not in graph):
                graph[u] = set()
            graph[u].add((v, t))
        
        
        visited = set()
        h = [(0, k)]

        while(h):
            t, v = hq.heappop(h)
            if(v in visited):
                continue
            visited.add(v)
            if(len(visited) == n):
                return t
            
            neigh = graph.get(v, set())
            for (v_, t_) in neigh:
                if(v_ not in visited):
                    hq.heappush(h, (t+t_, v_))
        return -1