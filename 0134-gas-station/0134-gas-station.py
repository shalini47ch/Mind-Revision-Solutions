class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalearning=sum(gas)
        totalexpenditure=sum(cost)
        if(totalexpenditure>totalearning):
            return -1
        total=0
        start=0
        for i in range(0,len(gas)):
            total=total+gas[i]-cost[i]
            if(total<0):
                start=i+1
                total=0
        return start



        