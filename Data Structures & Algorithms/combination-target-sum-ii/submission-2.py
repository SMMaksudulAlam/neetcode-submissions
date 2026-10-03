class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        track = set()
        ans = []
        def comb(rem, lst, ind): #1 2 2 2
            if(rem==0):
                ans.append(lst[:])
                return
            if(ind<0 or rem<0):
                return
            num = candidates[ind]
            if(rem-num>=0):
                comb(rem-num, lst+[num], ind-1)
            ind -= 1
            while(ind>=0 and candidates[ind]==candidates[ind+1]):
                ind-=1
            comb(rem, lst, ind)
            return
        
        comb(target, [], len(candidates)-1)
        return ans