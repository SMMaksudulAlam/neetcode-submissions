import heapq as hq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for u, v, c in flights:
            if(u not in graph):
                graph[u] = set()
            graph[u].add((v, c))

        h = [(0, 0, src)]
        visited = set()

        while(h):
            cst, stp, src = hq.heappop(h)
            if((stp, src) in visited):
                continue
            visited.add((stp, src))
            if(src == dst and stp<=k+1):
                return cst
            neigh = graph.get(src, set())
            for v, c in neigh:
                if(stp>=k+1 or (stp+1, v) in visited):
                    continue
                hq.heappush(h, (cst + c, stp+1, v))
        return -1


        
        