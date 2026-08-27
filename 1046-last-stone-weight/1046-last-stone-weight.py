import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #we need to return the weight of the last remaining stone and here we will use maxheap to solve this 
        maxheap=[]
        for i in range(0,len(stones)):
            heapq.heappush(maxheap,-stones[i])
        while(len(maxheap)>1):
            #x is the heaviest and then y
            x=-heapq.heappop(maxheap)
            y=-heapq.heappop(maxheap)
            heapq.heappush(maxheap,(y-x))
        return -maxheap[0] if maxheap else 0
       
       

        




       
       