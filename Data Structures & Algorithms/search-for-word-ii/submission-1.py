class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            cur_t = trie
            for ch in w:
                if(ch not in cur_t):
                    cur_t[ch] = {}
                cur_t = cur_t[ch]
            cur_t["end"] = w
        

        path = set()
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = set()

        def traverse(i, j, cur_t):
            if("end" in cur_t):
                ans.add(cur_t["end"])
            path.add((i, j))
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj
                if((0<=i_<len(board)) and (0<=j_<len(board[0])) and ((i_, j_) not in path) and board[i_][j_] in cur_t):
                    traverse(i_, j_, cur_t[board[i_][j_]])
            path.remove((i, j))
            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] in trie):
                    traverse(i, j, trie[board[i][j]])

        return list(ans)
