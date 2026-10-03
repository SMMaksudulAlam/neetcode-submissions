class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def traverse(i, j, ind):
            if((i, j) in path):
                return False
            if(ind>=len(word)):
                return True
            path.add((i, j))
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj
                if((0<=i_<len(board)) and (0<=j_<len(board[0])) and ((i_, j_) not in path) and board[i_][j_] == word[ind]):
                    if(traverse(i_, j_, ind+1)):
                        return True
            path.remove((i, j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == word[0]):
                    if(traverse(i, j, 1)):
                        return True
        return False

