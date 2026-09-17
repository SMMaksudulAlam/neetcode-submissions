class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = {}
        row = len(matrix)
        col = len(matrix[0])
        def dfs(i, j):
            if((i, j) in visited):
                return visited[(i, j)]
            left = matrix[i][j-1] if(j-1 >= 0) else -math.inf
            right = matrix[i][j+1] if(j+1 < col) else -math.inf
            up = matrix[i-1][j] if(i-1 >= 0) else -math.inf
            down = matrix[i+1][j] if(i+1 < row) else -math.inf

            val = matrix[i][j]
            visited[(i, j)] = 1
            if(left<=val and right<=val and up<=val and down <=val):
                return 1
            
            ans = 1
            if(left>val):
                ans = max(ans, 1 + dfs(i, j-1))
            if(right>val):
                ans = max(ans, 1 + dfs(i, j+1))
            if(up>val):
                ans = max(ans, 1 + dfs(i-1, j))
            if(down>val):
                ans = max(ans, 1 + dfs(i+1, j))
            visited[(i, j)] = ans
            return ans
        
        ans = 1
        for i in range(row):
            for j in range(col):
                if((i, j) not in visited):
                    ans = max(ans, dfs(i, j))
        return ans