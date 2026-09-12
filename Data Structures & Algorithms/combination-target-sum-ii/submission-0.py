class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        ans = []
        def build(target, cur, ind):
            if(target == 0):
                ans.append(cur[:])
                return
            if(ind<0):
                return
            if(target>=nums[ind]):
                build(target-nums[ind], cur+[nums[ind]], ind-1)
            while(ind>0 and nums[ind] == nums[ind-1]):
                ind-=1
                continue
            build(target, cur, ind-1)
            return
        build(target, [], len(nums)-1)
        return ans