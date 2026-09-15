class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x:x[0])
        till = intervals[0][1]


        ind = 1
        while(ind<len(intervals)):
            if(intervals[ind][0]<till):
                count += 1
                till = min(intervals[ind][1], till)
            else:
                till = intervals[ind][1]
            ind+=1
        return count