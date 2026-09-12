class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def build(ind):
            if(ind>=len(nums)):
                ans.append(sub[:])
                return
            sub.append(nums[ind])
            build(ind+1)
            sub.pop()
            build(ind+1)
            return
        build(0)
        return ans