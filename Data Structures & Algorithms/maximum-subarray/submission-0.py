class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm = nums[0]
        ans = sm
        for i in range(1, len(nums)):
            if(sm>=0):
                sm += nums[i]
            else:
                sm = nums[i]
            ans = max(ans, sm)
        return ans