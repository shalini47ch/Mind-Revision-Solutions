class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #use the concept of binary search on answer to solve 
        n=len(piles)
        start=1
        end=max(piles)
        res=-1
        while(start<=end):
            mid=start+(end-start)//2
            if(self.helper(piles,mid)<=h):
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
        
    def helper(self,piles,mid):
        su=0
        for i in range(0,len(piles)):
            su+=ceil(piles[i]/mid)
        return su







        