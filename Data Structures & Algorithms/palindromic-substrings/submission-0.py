class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            left = i-1
            right = i+1
            ans +=1
            while(left>=0 and right<len(s) and s[left]==s[right]):
                ans+=1
                left-=1
                right+=1

            if(i+1<len(s) and s[i]==s[i+1]):
                left = i-1
                right = i+2
                ans += 1
                while(left>=0 and right<len(s) and s[left]==s[right]):
                    ans += 1
                    left-=1
                    right+=1
                    
        return ans
