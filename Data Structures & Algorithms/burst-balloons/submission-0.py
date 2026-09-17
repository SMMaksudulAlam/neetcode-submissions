class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def burst(left, right):
            if(left+1 == right):
                return 0

            if((left, right) in dp):
                return dp[(left, right)]
            
            ans = 0
            for i in range(left+1, right):
                ans = max(ans, nums[left]*nums[i]*nums[right] + burst(left, i) + burst(i, right))
            
            
            dp[(left, right)] = ans
            return ans
        
        ans = burst(0, len(nums)-1)
        return ans