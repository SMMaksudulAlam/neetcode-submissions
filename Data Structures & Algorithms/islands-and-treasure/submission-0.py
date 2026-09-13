class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    q.append((i, j))
        
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dist = 0
        while(q):
            q_ = []
            while(q):
                (i, j) = q.pop()
                for (di, dj) in dir:
                    i_ = i+di
                    j_ = j+dj
                    if(0<=i_<len(grid) and 0<=j_<len(grid[0]) and grid[i_][j_]>dist+1):
                        grid[i_][j_] = dist + 1
                        q_.append((i_, j_))
            dist+=1
            q = q_
        return
