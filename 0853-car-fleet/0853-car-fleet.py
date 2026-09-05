class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        lasttime=0
        #now iterate through the cars
        for pos,sp in cars:
            time=(target-pos)/sp
            #now here is the case for fleet
            if(time>lasttime):
                #so here we need a new fleet
                fleet+=1
                lasttime=time
        return fleet
        