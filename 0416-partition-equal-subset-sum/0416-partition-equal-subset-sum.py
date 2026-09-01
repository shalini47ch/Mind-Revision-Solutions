class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        su=sum(nums)
        target=su//2
        dp=[[-1 for i in range(target+1)]for j in range(n+1)]
        if(su%2==1):
            return False
        return self.helper(n-1,nums,target,n,dp)

    def helper(self,ind,nums,target,n,dp):
        #we will move from n-1 to 0
        if(ind==0):
            if(nums[0]==target):
                return True
            else:
                return False
        if(dp[ind][target]!=-1):
            return dp[ind][target]
        #now there are two options notpick or pick
        notpick=self.helper(ind-1,nums,target,n,dp)
        pick=False
        if(nums[ind]<=target):
            pick=self.helper(ind-1,nums,target-nums[ind],n,dp)
        dp[ind][target]=(pick or notpick)
        return dp[ind][target]
        