class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def rob_(ind):
            if(ind in dp):
                return dp[ind]
            if(ind<0):
                return 0
            dp[ind] = max(nums[ind]+rob_(ind-2), rob_(ind-1))
            return dp[ind]
        
        return rob_(len(nums)-1)