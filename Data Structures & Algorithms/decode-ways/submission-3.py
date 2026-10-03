class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0]=='0'):
            return 0
        ans = [0]*len(s)
        ans[0] = 1

        if(len(s)>=2):
            num = int(s[:2])
            if(s[1]=='0'):
                if(num == 10 or num == 20):
                    ans[1] = 1
                else:
                    return 0
            else:
                if(11<=num<=26):
                    ans[1] = 2
                else:
                    ans[1] = 1
            
        for i in range(2, len(s)):
            num = int(s[i-1:i+1])
            if(s[i]=='0'):
                if(num == 10 or num == 20):
                    ans[i] = ans[i-2]
                else:
                    return 0
            else:
                ans[i] = ans[i-1]
                if(11<=num<=26):
                    ans[i]+=ans[i-2]
        return ans[-1]