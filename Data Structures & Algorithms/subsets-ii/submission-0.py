class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def build(sub, ind):
            if(ind>=len(nums)):
                ans.append(sub[:])
                return
            build(sub+[nums[ind]], ind+1)
            while(ind+1<len(nums) and nums[ind+1] == nums[ind]):
                ind+=1
            build(sub, ind+1)
            return
        build([], 0)
        return ans