class Solution:
    def jump(self, nums: List[int]) -> int:
        till = 0
        ind = 0
        count = 1
        if(len(nums)==1):
            return 0
        while(ind<=till):
            next_till = till
            while(ind<=till):
                next_till = max(next_till, ind + nums[ind])
                if(next_till >= len(nums)-1):
                    return count
                ind+=1
            if(till<next_till):
                count += 1
            till = next_till
        return count