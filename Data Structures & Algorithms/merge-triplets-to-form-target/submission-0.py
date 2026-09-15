class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0, 0, 0]
        for (i, j, k) in triplets:
            if(i<=target[0] and j<=target[1] and k<=target[2]):
                ans = [max(ans[0], i), max(ans[1], j), max(ans[2], k)]
                if(ans == target):
                    return True
        return False