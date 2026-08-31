class Solution:
    def rob(self, nums: List[int]) -> int:
        #this is much similar to house robber 1 but here its arranged in the form of a circle
        n=len(nums)
        dp1=[-1 for i in range(n+1)]
        dp2=[-1 for i in range(n+1)]
        if(n==1):
            return nums[0]
        if(n==2):
            return max(nums[0],nums[1])
        ele1=self.helper(0,nums,n-2,dp1)
        ele2=self.helper(1,nums,n-1,dp2)
        return max(ele1,ele2)


    def helper(self,ind,nums,n,dp):
        if(ind>n):
            return 0
        if(dp[ind]!=-1):
            return dp[ind]
        #there are two options either dont rob that house or rob that house
        notpick=self.helper(ind+1,nums,n,dp)
        pick=nums[ind]+self.helper(ind+2,nums,n,dp)
        dp[ind]=max(pick,notpick)
        return dp[ind]
        