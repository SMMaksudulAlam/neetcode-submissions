class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if(len1 + len2 != len3):
            return False

        dp = {}
        def check(ind1, ind2, ind3):
            if((ind1, ind2, ind3) in dp):
                return dp[(ind1, ind2, ind3)]
            if(ind1<0 and ind2<0 and ind3<0):
                return True
            
            ans = False
            if(ind3>=0 and ind1>=0 and s3[ind3]==s1[ind1]):
                ans = ans or check(ind1-1, ind2, ind3-1)
            if(ind3>=0 and ind2>=0 and s3[ind3]==s2[ind2]):
                ans = ans or check(ind1, ind2-1, ind3-1)
            
            dp[(ind1, ind2, ind3)] = ans
            return ans
        
        ans = check(len1-1, len2-1, len3-1)
        return ans

        