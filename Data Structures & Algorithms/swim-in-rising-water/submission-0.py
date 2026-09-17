import heapq as hq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = []
        ans = 0
        h.append((grid[0][0], (0, 0)))
        visited = set()

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ln = len(grid)
        while(h):
            time, (x, y) = hq.heappop(h)
            if((x, y) in visited):
                continue
            
            ans = max(ans, time)
            visited.add((x, y))

            if(x == ln-1 and y == ln-1):
                return ans
            for (dx, dy) in dir:
                x_ = x+dx
                y_ = y+dy
                if((x_, y_) in visited):
                    continue
                if(0<=x_<ln and 0<=y_<ln):
                    hq.heappush(h, (grid[x_][y_], (x_, y_)))
        return -1

