class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            dic = trie
            for ch in word:
                if(ch not in dic):
                    dic[ch] = {}
                dic = dic[ch]
            dic["end"] = word
        
        #print(trie)
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        path = set()
        ans = set()
        row = len(board)
        col = len(board[0])
        def dfs(i, j, dic):
            if((i, j) in path):
                return 
            if("end" in dic):
                ans.add(dic['end'])
            
            path.add((i, j))
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj
                if(0<=i_<row and 0<=j_<col and board[i_][j_] in dic):
                    dfs(i_, j_, dic[board[i_][j_]])
            
            path.remove((i, j))
            return 
        
        for i in range(row):
            for j in range(col):
                if(board[i][j] in trie):
                    dfs(i, j, trie[board[i][j]])
        return list(ans)