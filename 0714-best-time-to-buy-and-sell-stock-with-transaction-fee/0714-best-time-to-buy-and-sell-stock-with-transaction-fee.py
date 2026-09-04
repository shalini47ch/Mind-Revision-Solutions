class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #here we need to return the max profit we can achieve but need to pay transaction fee for each transaction
        n=len(prices)
        dp=[[-1 for i in range(2)]for j in range(n+1)]
        return self.helper(0,1,prices,fee,n,dp)

    def helper(self,ind,buy,prices,fee,n,dp):
        if(ind==n):
            return 0
        if(dp[ind][buy]!=-1):
            return dp[ind][buy]
        if(buy):
            profit=max(-prices[ind]+self.helper(ind+1,0,prices,fee,n,dp),
            0+self.helper(ind+1,1,prices,fee,n,dp))
        else:
            profit=max(prices[ind]-fee+self.helper(ind+1,1,prices,fee,n,dp),
            0+self.helper(ind+1,0,prices,fee,n,dp))
        dp[ind][buy]=profit
        return dp[ind][buy]







    
        