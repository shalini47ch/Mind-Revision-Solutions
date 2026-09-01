import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #since we need to  find the top k frequent elements so we will use hmap+minheap to solve this 
        #lets first find the freq of the elements 
        hmap=defaultdict(int)
        for i in range(0,len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]]=1
            else:
                hmap[nums[i]]+=1
        minheap=[]
        for key,val in hmap.items():
            heapq.heappush(minheap,[val,key])
            if(len(minheap)>k):
                heapq.heappop(minheap)
        ans=[] #here we will return the final answer that is the keys 
        while(len(minheap)>0):
            ele=heapq.heappop(minheap)
            ans.append(ele[1])
        return ans
       