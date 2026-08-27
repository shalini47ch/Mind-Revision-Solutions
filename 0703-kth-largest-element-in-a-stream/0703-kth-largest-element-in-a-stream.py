class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #use minheap to solve this 
        self.k=k
        self.minheap=[]
        for ele in nums:
            self.add(ele)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        while(len(self.minheap)>self.k):
            heapq.heappop(self.minheap)
        return self.minheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)