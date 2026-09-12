class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ind = abs(nums[i])
            if(nums[ind]<0):
                return ind
            nums[ind] = -nums[ind]
        return -1
        """
        fast = 0
        slow = 0
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(fast == slow):
                break
        
        slow = 0
        while(True):
            slow = nums[slow]
            fast = nums[fast]
            if(fast == slow):
                return slow
        return -1
        """
