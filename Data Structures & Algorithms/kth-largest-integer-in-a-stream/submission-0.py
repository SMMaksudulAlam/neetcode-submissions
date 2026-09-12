import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for n in nums:
            if(len(self.h)<k):
                hq.heappush(self.h, n)
            else:
                if(n>self.h[0]):
                    hq.heappop(self.h)
                    hq.heappush(self.h, n)

    def add(self, val: int) -> int:
        if(len(self.h)<self.k):
            hq.heappush(self.h, val)
        else:
            if(val>self.h[0]):
                hq.heappop(self.h)
                hq.heappush(self.h, val)
        return self.h[0]
