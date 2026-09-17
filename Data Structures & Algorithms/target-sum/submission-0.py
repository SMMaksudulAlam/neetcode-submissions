class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def find_sum(rem, ind):
            if((rem, ind) in dp):
                return dp[(rem, ind)]
            if(ind<0):
                if(rem == 0):
                    return 1
                return 0
            ans = 0
            ans += find_sum(rem+nums[ind], ind-1)
            ans += find_sum(rem-nums[ind], ind-1)

            dp[(rem, ind)] = ans
            return ans
        
        return find_sum(target, len(nums)-1)