class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = 'x'+s
        ans = [False]*(len(s))
        ans[0] = True

        for i in range(len(ans)):
            if(ans[i] == True):
                for w in wordDict:
                    if(i+len(w) < len(ans) and s[i+1:i+len(w)+1] == w):
                        ans[i+len(w)] = True
                        if(ans[-1]==True):
                            return True
        return False
