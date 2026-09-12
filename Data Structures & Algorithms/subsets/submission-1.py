class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def build(sub, ind):
            if(ind>=len(nums)):
                ans.append(sub[:])
                return
            build(sub+[nums[ind]], ind+1)
            build(sub, ind+1)
            return
        build([], 0)
        return ans