class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1 for i in range(n+1)]
        ele1=self.helper(n-1,cost,dp)
        ele2=self.helper(n-2,cost,dp)
        return min(ele1,ele2)

    def helper(self,ind,cost,dp):
        if(ind<=1):
            return cost[ind]
        if(dp[ind]!=-1):
            return dp[ind]
        #onestep or twostep
        onestep=cost[ind]+self.helper(ind-1,cost,dp)
        twostep=cost[ind]+self.helper(ind-2,cost,dp)
        dp[ind]=min(onestep,twostep)
        return dp[ind]
       