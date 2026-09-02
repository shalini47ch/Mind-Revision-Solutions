class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #this can be solved using recursion+memo
        #here we need to return the no of different expressions 
        n=len(nums)
        totalsum=sum(nums)
        dp=[[-1 for i in range(2*totalsum+1)]for j in range(n+1)]
        return self.helper(0,nums,0,target,totalsum,n,dp)

    def helper(self,ind,nums,currsum,target,totalsum,n,dp):
        #we will move from index 0 till n
        if(ind==n):
            if(currsum==target):
                return 1
            else:
                return 0
        if(dp[ind][currsum]!=-1):
            return dp[ind][currsum]
        #now there are two options either add or sub
        add=self.helper(ind+1,nums,currsum+nums[ind],target,totalsum,n,dp)
        sub=self.helper(ind+1,nums,currsum-nums[ind],target,totalsum,n,dp)
        dp[ind][currsum]=(add+sub)
        return dp[ind][currsum]









    

        