class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def lcs(ind1, ind2):
            if(ind1<0 or ind2<0):
                return 0
            if((ind1, ind2) in dp):
                return dp[(ind1, ind2)]
            if(text1[ind1] == text2[ind2]):
                dp[(ind1, ind2)] =  1 + lcs(ind1-1, ind2-1)
                return dp[(ind1, ind2)]
            dp[(ind1, ind2)] = max(lcs(ind1-1, ind2), lcs(ind1, ind2-1), lcs(ind1-1, ind2-1))
            return dp[(ind1, ind2)]
        
        return lcs(len(text1)-1, len(text2)-1)