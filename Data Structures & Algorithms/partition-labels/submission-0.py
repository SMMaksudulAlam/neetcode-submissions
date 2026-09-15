class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ranges = {}
        for i, e in enumerate(s):
            if(e not in ranges):
                ranges[e] = [i, i]
            else:
                ranges[e][-1] = i
        
        ans = []
        ind = 0
        while(ind<len(s)):
            count = 0
            e = s[ind]
            right_limit = ranges[e][1]
            while(ind<=right_limit):
                e = s[ind]
                right_limit = max(right_limit, ranges[e][1])
                ind+=1
                count += 1
            ans.append(count)
        return ans