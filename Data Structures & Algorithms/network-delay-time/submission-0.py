import heapq as hq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: set() for i in range(1, n+1)}
        for (u, v, t) in times:
            graph[u].add((v, t))
        
        h = [(0, k)]
        ans = 0
        visited = set()
        while(h):
            (time, u) = hq.heappop(h)
            if(u in visited):
                continue
            
            ans = time
            visited.add(u)
            if(len(visited) == n):
                return ans
            
            for (v, t) in graph.get(u, []):
                if(v not in visited):
                    hq.heappush(h, (time+t, v))
            
        return -1