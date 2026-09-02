import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use the concept of maxheap to solve this 
        maxheap=[]
        for i in range(0,len(points)):
            x=points[i][0]
            y=points[i][1]
            heapq.heappush(maxheap,[-x*x-y*y,x,y])
            if(len(maxheap)>k):
                heapq.heappop(maxheap)
        #so here at last we need to return the coordinates
        return [[x,y] for dis,x,y in maxheap]
       
        

      


        