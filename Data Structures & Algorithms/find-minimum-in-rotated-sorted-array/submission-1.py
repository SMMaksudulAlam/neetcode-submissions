class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==1 or nums[0]<nums[-1]):
            return nums[0]
        if(nums[-2]>nums[-1] and nums[-1]<nums[0]):
            return nums[-1]
        
        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2
            if(nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]):
                return nums[mid]
            if(nums[mid]<nums[right]):
                right = mid-1
            else:
                left = mid+1
        return -1
