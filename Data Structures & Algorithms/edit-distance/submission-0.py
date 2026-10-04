class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def edit(ind1, ind2):
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(ind1<0):
                return max(0, ind2+1)
            if(ind2<0):
                return max(0, ind1+1)
            
            if(word1[ind1]==word2[ind2]):
                ans = edit(ind1-1, ind2-1)
                dp[(ind1, ind2)] = ans
                return ans
            ans = 1+min(edit(ind1-1, ind2), edit(ind1, ind2-1), edit(ind1-1, ind2-1))
            dp[(ind1, ind2)] = ans
            return ans
        
        return edit(len(word1)-1, len(word2)-1)