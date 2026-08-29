class Solution:
    def jump(self, nums: List[int]) -> int:
        #so here we need to return the minimum no of jumps to reach the end
        farthest=0
        currend=0
        jumps=0
        #traverse through the nums array
        for i in range(0,len(nums)-1):
            farthest=max(farthest,nums[i]+i)
            if(i==currend):
                jumps+=1
                currend=farthest
        return jumps


       