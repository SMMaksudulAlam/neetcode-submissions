class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(i, j):
            if(grid[i][j] == 0):
                return 0
            ans = 1
            grid[i][j] = 0
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj
                if(0<=i_<len(grid) and 0<=j_<len(grid[0]) and grid[i_][j_] == 1):
                    ans += dfs(i_, j_)
            return ans
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    ans = max(ans, dfs(i, j))
        return ans