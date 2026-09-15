class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if(not intervals):
            return [newInterval]

        ans = []
        ind = 0
        while(ind<len(intervals) and intervals[ind][0]<=newInterval[0]):
            ans.append(intervals[ind])
            ind+=1

        if(ans and ans[-1][1]>=newInterval[0]):
            ans[-1][1] = max(ans[-1][1], newInterval[1])
        else:
            ans.append(newInterval)

        while(ind<len(intervals)):
            if(ans[-1][1]>=intervals[ind][0]):
                ans[-1][1] = max(ans[-1][1], intervals[ind][1])
            else:
                ans.append(intervals[ind])
            ind+=1
        
        return ans
