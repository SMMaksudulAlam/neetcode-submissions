import heapq as hq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []
        ans = 0
        visited = set()
        h.append((0, (points[0][0], points[0][1])))

        def helper(x, y, x_, y_):
            return abs(x-x_)+abs(y-y_)

        while(h):
            dis, (x, y) = hq.heappop(h)
            if((x, y) in visited):
                continue
            ans += dis
            visited.add((x, y))
            if(len(visited) == len(points)):
                return ans
            
            for (x_, y_) in points:
                if((x_, y_) in visited):
                    continue
                dis_ = helper(x, y, x_, y_)
                hq.heappush(h, (dis_, (x_, y_)))
        return ans