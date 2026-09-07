import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #this is based on the concept of kadanes algorithm and if the value in nums is negative we need to swap the maxprod and minprod
        currmax=nums[0]
        currmin=nums[0]
        maxi=nums[0]
        #now lets iterate through the nums array from 1 till n
        for x in nums[1:]:
            if(x<0):
                currmin,currmax=currmax,currmin
            currmax=max(x,currmax*x)
            currmin=min(x,currmin*x)
            maxi=max(maxi,currmax)
        return maxi

        