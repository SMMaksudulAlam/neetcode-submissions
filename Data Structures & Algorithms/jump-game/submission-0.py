class Solution:
    def canJump(self, nums: List[int]) -> bool:
        till = 0
        ind = 0

        while(ind<=till):
            next_till = till
            while(ind<=till):
                next_till = max(next_till, ind + nums[ind])
                if(next_till >= len(nums)-1):
                    return True
                ind+=1
            till = next_till
        return False