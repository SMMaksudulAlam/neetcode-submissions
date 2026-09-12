class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def build(target, cur, ind):
            if(target == 0):
                ans.append(cur[:])
                return
            if(ind<0):
                return
            if(target>=nums[ind]):
                build(target-nums[ind], cur+[nums[ind]], ind)

            build(target, cur, ind-1)
            return
        build(target, [], len(nums)-1)
        return ans