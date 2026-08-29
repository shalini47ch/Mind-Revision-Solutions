class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #here we need to return True if we can reach the last index else False otherwise
        n=len(nums)
        farthest=0
        for i in range(0,n):
            if(i>farthest):
                return False 
            farthest=max(farthest,i+nums[i])
        return True

       
        