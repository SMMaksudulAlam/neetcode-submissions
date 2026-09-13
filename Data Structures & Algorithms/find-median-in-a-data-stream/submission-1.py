import heapq as hq
class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def balance(self):
        while(len(self.right)>len(self.left)+1):
            hq.heappush(self.left, -hq.heappop(self.right))
        
        while(len(self.left)>len(self.right)):
            hq.heappush(self.right, -hq.heappop(self.left))

    def addNum(self, num: int) -> None:
        if(not self.right):
            self.right.append(num)
            return
        
        if(num>=self.right[0]):
            hq.heappush(self.right, num)
        else:
            hq.heappush(self.left, -num)
        self.balance()
        return

    def findMedian(self) -> float:
        #print(self.left ,self.right)
        if((len(self.left)+len(self.right))%2==1):
            return self.right[0]
        return (self.right[0] - self.left[0])/2.0

        