class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=nums[0]
        maxsum=nums[0]
        #this is kadanes algo
        for i in range(1,len(nums)):
            if(currsum>0):
                currsum+=nums[i]
            else:
                currsum=nums[i]
            maxsum=max(maxsum,currsum)
        return maxsum
        
       