class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        high = nums[0]
        low = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp = high
            high = max(high*num, low*num, num)
            low = min(temp*num, low*num, num)
            ans = max(ans, high)

        return ans