class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #return the max profit you can achieve
        n=len(prices)
        dp=[[-1 for i in range(2)]for j in range(n+1)]
        return self.helper(0,1,prices,n,dp)

    def helper(self,ind,buy,prices,n,dp):
        if(ind==n):
            return 0
        if(dp[ind][buy]!=-1):
            return dp[ind][buy]
        if(buy):
            profit=max(-prices[ind]+self.helper(ind+1,0,prices,n,dp),
            0+self.helper(ind+1,1,prices,n,dp))
        else:
            profit=max(prices[ind]+self.helper(ind+1,1,prices,n,dp),
            0+self.helper(ind+1,0,prices,n,dp))
        dp[ind][buy]=profit
        return dp[ind][buy]
      