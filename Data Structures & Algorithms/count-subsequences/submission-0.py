class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def count(ind_s, ind_t):
            if((ind_s, ind_t) in dp):
                return dp[(ind_s, ind_t)]
            if(ind_t < 0):
                return 1
            if(ind_s<0):
                return 0
            
            ans = 0
            if(s[ind_s]==t[ind_t]):
                ans = count(ind_s-1, ind_t-1)
            
            ans += count(ind_s-1, ind_t)
            dp[(ind_s, ind_t)] = ans
            return ans
        
        ans = count(len(s)-1, len(t)-1)
        return ans