class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        count = 0
        tank = 0
        ind = 0

        while(True):
            count += 1
            if(count == len(gas)+1):
                return start
            tank += (gas[ind] - cost[ind])
            if(tank>=0):
                ind = (ind+1)%len(gas)
            else:
                next_start = (ind+1)%len(gas)
                if(next_start <= start):
                    return -1
                start = next_start
                count = 0
                tank = 0
                ind = start
        return -1
