class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def wBreak(ind):
            if(ind in dp):
                return dp[ind]
            if(ind == -1):
                return True
            for w in wordDict:
                ln = len(w)
                if(ind-ln+1>=0 and w == s[ind-ln+1:ind+1]):
                    if(wBreak(ind-ln)):
                        dp[ind] = True
                        return True
            dp[ind] = False
            return False
        
        return wBreak(len(s)-1)