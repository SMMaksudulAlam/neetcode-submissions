import heapq as hq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = []
        ans = 0
        h.append((grid[0][0], 0, 0))

        visited = set()
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while(h):
            time, i, j = hq.heappop(h)
            if((i, j) in visited):
                continue
            visited.add((i, j))
            if(i==len(grid)-1 and j==len(grid[0])-1):
                return time

            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj
                if(0<=i_<len(grid) and 0<=j_<len(grid[0]) and ((i_, j_) not in visited)):
                    hq.heappush(h, (max(grid[i_][j_], time), i_, j_))
        return -1