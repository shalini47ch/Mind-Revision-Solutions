class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails=[]
        for num in nums:
            ind=bisect.bisect_left(tails,num)
            if(ind==len(tails)):
                tails.append(num)
            else:
                tails[ind]=num
        return len(tails)
    
    
    
    
    
    #     n=len(nums)
    #     dp=[[-1 for i in range(n+1)]for j in range(n+1)]
    #     return self.helper(0,-1,nums,n,dp)

    # def helper(self,ind,prev,nums,n,dp):
    #     if(ind==n):
    #         return 0
    #     if(dp[ind][prev+1]!=-1):
    #         return dp[ind][prev+1]
    #     notpick=self.helper(ind+1,prev,nums,n,dp)
    #     pick=0
    #     if(prev==-1 or nums[ind]>nums[prev]):
    #         pick=1+self.helper(ind+1,ind,nums,n,dp)
    #     dp[ind][prev+1]=max(pick,notpick)
    #     return dp[ind][prev+1]

       