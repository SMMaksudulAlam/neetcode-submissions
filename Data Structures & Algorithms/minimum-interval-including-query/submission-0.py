import heapq as hq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        intervals = deque(intervals)
        queries_ = queries[:]
        queries_.sort()
        queries_ = deque(queries_)

        dic = {}
        h = []
        
        while(queries_):
            while(intervals and intervals[0][0]<=queries_[0]):
                interval = intervals.popleft()
                if(interval[1]>=queries_[0]):
                    hq.heappush(h, (interval[1]-interval[0]+1, interval[1]))
            
            while(h and queries_ and h[0][1]<queries_[0]):
                hq.heappop(h)
            if(h):
                dic[queries_[0]] = h[0][0]
            queries_.popleft()

        ans = []
        for q in queries:
            val = dic.get(q, -1)
            ans.append(val)
        
        return ans