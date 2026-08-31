class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]
        for i in range(0,len(nums)):
            heapq.heappush(minheap,nums[i])
        while(len(minheap)>k):
            heapq.heappop(minheap)
        return minheap[0]


       