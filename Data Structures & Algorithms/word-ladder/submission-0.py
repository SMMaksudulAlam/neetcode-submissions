class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        patterns = {}
        for w in wordList:
            for i in range(len(w)):
                s = w[:i]+'*'+w[i+1:]
                if(s not in patterns):
                    patterns[s] = set()
                patterns[s].add(w)
        
        #print(patterns)
        visited = set()
        count = 1
        q = [beginWord]
        visited.add(beginWord)

        while(q):
            q_ = []
            while(q):
                w = q.pop()
                if(w == endWord):
                    return count
                for i in range(len(w)):
                    s = w[:i]+'*'+w[i+1:]
                    neigh = patterns[s]
                    for n in neigh:
                        if(n not in visited):
                            visited.add(n)
                            q_.append(n)
            count += 1
            q = q_
        return 0
                

