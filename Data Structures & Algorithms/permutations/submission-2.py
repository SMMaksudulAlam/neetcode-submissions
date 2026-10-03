class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(nums):
            if(len(nums)==1):
                return [nums[:]]
            ln = len(nums)
            ans = []
            for i in range(ln):
                e = nums.pop()
                temp_ans = perm(nums[:])
                for ans_ in temp_ans:
                    ans.append(ans_+[e])
                nums = [e] + nums
            return ans
        return perm(nums)