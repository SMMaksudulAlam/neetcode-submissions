class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def build(left, right):
            if(not right):
                ans.append(left)
                return
            for i, e in enumerate(right):
                build(left+[e], right[:i]+right[i+1:])
            return
        build([], nums)
        return ans
                