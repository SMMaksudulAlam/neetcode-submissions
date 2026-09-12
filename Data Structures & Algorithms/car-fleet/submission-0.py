class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count  = 0
        ar = [[position[i], speed[i]] for i in range(len(position))]
        ar.sort(key = lambda x:x[0])

        time = 0
        for i in range(len(ar)-1, -1, -1):
            t = (target-ar[i][0])/ar[i][1]
            if(t>time):
                time = t
                count+=1
        return count


