class Solution:
    def climbStairs(self, n: int) -> int:
        #there are two options we can either jump one step or two step
        dp=[-1 for i in range(n+1)]
        return self.helper(n,dp)

    def helper(self,n,dp):
        #if you are on the ground floor you can stay there so 1
        if(n==0):
            return 1
        if(n<0):
            return 0
        if(dp[n]!=-1):
            return dp[n]
        #now there are two options either onestep or twostep
        onestep=self.helper(n-1,dp)
        twostep=self.helper(n-2,dp)
        dp[n]=(onestep+twostep)
        return dp[n]
       