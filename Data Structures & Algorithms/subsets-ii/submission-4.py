class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def sub(lst, ind):
            if(ind<0):
                ans.append(lst[:])
                return
            num = nums[ind]
            sub(lst+[num], ind-1)
            while(ind>0 and nums[ind-1]==nums[ind]):
                ind-=1
            sub(lst, ind-1)
            return

        sub([], len(nums)-1)
        return ans