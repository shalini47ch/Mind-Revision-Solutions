import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        start=0
        end=n-1
        mini=sys.maxsize
        while(start<=end):
            mid=start+(end-start)//2
            if(nums[start]<=nums[mid]):
                mini=min(mini,nums[start])
                start=mid+1
            else:
                mini=min(mini,nums[mid])
                end=mid-1
        return mini
       