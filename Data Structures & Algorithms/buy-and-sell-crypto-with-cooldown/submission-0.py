class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def profit(ind, can_buy):
            if((ind, can_buy) in dp):
                return dp[(ind, can_buy)]
            if(ind>=len(prices)):
                return 0
            if(can_buy):
                ans1 = profit(ind+1, False) - prices[ind]
                ans2 = profit(ind+1, True)
                dp[(ind, can_buy)] = max(ans1, ans2)
                return dp[(ind, can_buy)]
            else:
                ans1 = profit(ind+2, True) + prices[ind]
                ans2 = profit(ind+1, False)
                dp[(ind, can_buy)] =  max(ans1, ans2)
                return dp[(ind, can_buy)]
            return 0
        
        ans = profit(0, True)
        return ans