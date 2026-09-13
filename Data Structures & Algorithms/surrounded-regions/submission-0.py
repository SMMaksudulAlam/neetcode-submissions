class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edge_o = set()
        row = len(board)
        col = len(board[0])
        for i in range(col):
            if(board[0][i]=='O'):
                edge_o.add((0, i))
        for i in range(col):
            if(board[row-1][i]=='O'):
                edge_o.add((row-1, i))

        for i in range(row):
            if(board[i][0]=='O'):
                edge_o.add((i, 0))

        for i in range(row):
            if(board[i][col-1]=='O'):
                edge_o.add((i, col-1))

        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
        def dfs(i, j):
            if(board[i][j]!='O'):
                return
            board[i][j] = 'P'
            for (di, dj) in dir:
                    i_ = i+di
                    j_ = j+dj
                    if(0<=i_<row and 0<=j_<col and board[i_][j_]=='O'):
                        dfs(i_, j_)
            return 
        
        for (i, j) in edge_o:
            dfs(i, j)
        
        for i in range(row):
            for j in range(col):
                if(board[i][j]=='O'):
                    board[i][j] = 'X'
                if(board[i][j]=='P'):
                    board[i][j] = 'O'
        return

