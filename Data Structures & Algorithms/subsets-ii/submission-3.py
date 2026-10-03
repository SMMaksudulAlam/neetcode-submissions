class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        new = [[]]

        for i, e in enumerate(nums):
            ans_ = ans[:]
            new_ = []
            if(i>0 and nums[i]==nums[i-1]):
                for n in new:
                    ans_.append(n+[e])
                    new_.append(n+[e])
                ans = ans_
                new = new_
                continue
            for a in ans:
                ans_.append(a+[e])
                new_.append(a+[e])
            ans = ans_
            new = new_
        return ans