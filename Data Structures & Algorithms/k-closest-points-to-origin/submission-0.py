import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
            x = p[0]
            y = p[1]
            return math.sqrt(x*x + y*y)
        h = []
        for p in points:
            dist = distance(p)
            if(len(h)<k):
                hq.heappush(h, (-dist, p))
            else:
                top = -h[0][0]
                if(dist<top):
                    hq.heappop(h)
                    hq.heappush(h, (-dist, p))
        ans = []
        for (d, p) in h:
            ans.append(p)
        return ans
