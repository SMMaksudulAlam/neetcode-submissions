class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def area_estimate(i, j):
            grid[i][j] = 0
            count = 1
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj
                if(0<=i_<len(grid) and 0<=j_<len(grid[0]) and grid[i_][j_]==1):
                    count += area_estimate(i_, j_)
            return count
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    ans = max(ans, area_estimate(i, j))
        return ans