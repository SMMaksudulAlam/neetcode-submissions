class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dsub(ind1, ind2):
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(ind2<0):
                return 1
            if(ind1<0):
                return 0
            
            ans = 0
            if(s[ind1]==t[ind2]):
                ans += dsub(ind1-1, ind2-1)
            ans += dsub(ind1-1, ind2)
            dp[(ind1, ind2)] = ans
            return ans
        
        return dsub(len(s)-1, len(t)-1)