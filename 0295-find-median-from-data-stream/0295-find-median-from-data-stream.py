class MedianFinder:

    def __init__(self):
        #use two heaps one is left that will be maxheap and the other is right that is minheap
        self.left=[] #this is maxheap
        self.right=[] #this is minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        heapq.heappush(self.right,-heapq.heappop(self.left))
        #now do the balance
        if(len(self.left)<len(self.right)):
            heapq.heappush(self.left,-heapq.heappop(self.right))
        
    def findMedian(self) -> float:
        #now here lets find the median
        if(len(self.left)>len(self.right)):
            return -self.left[0]
        return (-self.left[0]+self.right[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()