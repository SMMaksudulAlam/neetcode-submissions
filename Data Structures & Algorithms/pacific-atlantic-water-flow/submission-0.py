class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = [(0, i) for i in range(len(heights[0]))]
        q += [(i, 0) for i in range(1, len(heights))]
        pacific = set(q)

        while(q):
            q_ = []
            while(q):
                (i, j) = q.pop()
                for (di, dj) in dir:
                    i_ = i+di
                    j_ = j+dj
                    if((i_, j_) in pacific):
                        continue
                    if(0<=i_<len(heights) and 0<=j_<len(heights[0]) and heights[i_][j_]>=heights[i][j]):
                        q_.append((i_, j_))
                        pacific.add((i_, j_))
            q = q_
        #print(pacific)

        q = [(len(heights)-1, i) for i in range(len(heights[0]))]
        q += [(i, len(heights[0])-1) for i in range(len(heights)-1)]
        atlantic = set(q)
        #print(pacific)

        while(q):
            q_ = []
            while(q):
                (i, j) = q.pop()
                for (di, dj) in dir:
                    i_ = i+di
                    j_ = j+dj
                    if((i_, j_) in atlantic):
                        continue
                    if(0<=i_<len(heights) and 0<=j_<len(heights[0]) and heights[i_][j_]>=heights[i][j]):
                        q_.append((i_, j_))
                        atlantic.add((i_, j_))
            q = q_
        
        ans = []
        for p in pacific:
            if(p in atlantic):
                ans.append(list(p))
        return ans

