"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq as hq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if(not intervals):
            return 0
        h = [-1]
        count = 1
        intervals.sort(key = lambda x:x.start)

        for i in range(len(intervals)):
            s = intervals[i].start
            e = intervals[i].end

            if(h[0]<=s):
                hq.heappop(h)
                hq.heappush(h, e)
            else:
                count += 1
                hq.heappush(h, e)
        return count
                