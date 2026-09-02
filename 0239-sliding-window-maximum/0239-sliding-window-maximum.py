from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #here we need to return the maximum in sliding window so we will use deque to solve this 
        dq=deque()
        res=[]
        n=len(nums)
        for i in range(0,n):
            while dq and dq[0]<=i-k:
                #means we have not reached the window
                dq.popleft()
            #now we maintain monotonic decreasing
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if(i>=k-1):
                res.append(nums[dq[0]])
        return res
        