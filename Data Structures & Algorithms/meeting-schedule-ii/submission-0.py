"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        days = []
        for inrtvl in intervals:
            if(len(days)==0):
                days.append([inrtvl.start, inrtvl.end])
            else:
                done = False
                for i, day in enumerate(days):
                    if(day[-1]<=inrtvl.start):
                        days[i] = [inrtvl.start, inrtvl.end]
                        done = True
                        break
                if(not done):
                    days.append([inrtvl.start, inrtvl.end])
        return len(days)
        