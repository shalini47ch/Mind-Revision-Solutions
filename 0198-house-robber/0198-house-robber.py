class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1 for i in range(n+1)]
        return self.helper(0,nums,n,dp)

    def helper(self,ind,nums,n,dp):
        #we will move from 0 till n
        if(ind>=n):
            return 0
        if(dp[ind]!=-1):
            return dp[ind]
        notpick=self.helper(ind+1,nums,n,dp)
        pick=nums[ind]+self.helper(ind+2,nums,n,dp)
        dp[ind]=max(pick,notpick)
        return dp[ind]
        