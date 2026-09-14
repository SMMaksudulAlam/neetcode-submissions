class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = math.inf
        dp = {}
        def change(rem, ind):
            if((rem, ind) in dp):
                return dp[(rem, ind)]
            if(rem==0):
                return 0
            if(ind<0):
                return math.inf
            
            ans = math.inf
            if(rem>=coins[ind]):
                ans = 1 + change(rem-coins[ind], ind)
            
            ans = min(ans, change(rem, ind-1))
            dp[(rem, ind)] = ans
            return dp[(rem, ind)]
        
        ans = change(amount, len(coins)-1)
        return ans if ans != math.inf else -1

