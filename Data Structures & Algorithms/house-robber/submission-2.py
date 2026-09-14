class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def rob_(ind):
            if(ind in dp):
                return dp[ind]
            if(ind==0):
                return nums[0]
            if(ind==1):
                return max(nums[0], nums[1])
            dp[ind] = max(nums[ind]+rob_(ind-2), rob_(ind-1))
            return dp[ind]
        
        return rob_(len(nums)-1)