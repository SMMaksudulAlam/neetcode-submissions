class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            left = i-1
            right = i+1
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
            
            if(len(ans)<right-left-1):
                ans = s[left+1:right]

            if(i+1<len(s) and s[i]==s[i+1]):
                left = i-1
                right = i+2
                while(left>=0 and right<len(s) and s[left]==s[right]):
                    left-=1
                    right+=1
                
                if(len(ans)<right-left-1):
                    ans = s[left+1:right]
        return ans
