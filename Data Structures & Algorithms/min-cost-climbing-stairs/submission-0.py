class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def climb(ind):
            if(ind in dp):
                return dp[ind]
            if(ind == 0 or ind == 1):
                return 0
            dp[ind] = min(cost[ind-1]+climb(ind-1), cost[ind-2]+climb(ind-2))
            return dp[ind]
        return climb(len(cost))

            
