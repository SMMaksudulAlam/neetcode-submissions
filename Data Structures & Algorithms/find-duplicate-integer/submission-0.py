class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ind = abs(nums[i])-1
            if(nums[ind]<0):
                return ind+1
            nums[ind] = -nums[ind]
        return -1
