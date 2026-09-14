class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        cur_limit = 0
        ans = 0
        if(len(nums)==1):
            return 0
        while(cur<=cur_limit):
            next_limit = cur_limit
            while(cur<=cur_limit):
                jmp = nums[cur]
                next_limit = max(next_limit, cur+jmp)
                if(next_limit>=len(nums)-1):
                    return ans + 1
                cur+=1
            if(cur_limit < next_limit):
                ans += 1
            cur_limit = next_limit

        return False