class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def climb(ind):
            if(ind in dp):
                return dp[ind]
            if(ind==0):
                return 1
            if(ind==1):
                return 1
            
            dp[ind] = climb(ind-1) + climb(ind-2)
            return dp[ind]
        return climb(n)