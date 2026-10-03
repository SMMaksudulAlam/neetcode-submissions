class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def comb(rem, lst, ind):
            if(rem == 0):
                ans.append(lst[:])
                return
            if(ind<0 or rem<0):
                return
            num = nums[ind]
            if(rem-num>=0):
                comb(rem-num, lst+[num], ind)
            comb(rem, lst, ind-1)
            return
        comb(target, [], len(nums)-1)
        return ans