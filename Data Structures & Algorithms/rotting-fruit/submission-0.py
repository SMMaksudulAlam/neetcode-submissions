class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        time = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    q.append((i, j))
                    visited.add((i, j))
        
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while(q):
            q_ = []
            while(q):
                (i, j) = q.pop()
                for (di, dj) in dir:
                    i_ = di+i
                    j_ = dj+j
                    if(0<=i_<len(grid) and 0<=j_<len(grid[0]) and grid[i_][j_] == 1 and ((i_, j_) not in visited)):
                        q_.append((i_, j_))
                        visited.add((i_, j_))
            if(q_):
                time+=1
                q = q_
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if((i, j) not in visited and grid[i][j] == 1):
                    return -1
        return time