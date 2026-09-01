class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #here we need to return the minimum no of coins 
        #use recursion+memo to solve this 
        n=len(coins)
        dp=[[-1 for i in range(amount+1)]for j in range(n+1)]
        y=self.helper(n-1,coins,amount,n,dp)
        return y if y!=sys.maxsize else -1

    def helper(self,ind,coins,amount,n,dp):
        if(ind==0):
            if(amount%coins[ind]==0):
                return amount//coins[ind]
            else:
                return sys.maxsize
        if(dp[ind][amount]!=-1):
            return dp[ind][amount]
        #there are two options either to pick or notpick
        notpick=self.helper(ind-1,coins,amount,n,dp)
        pick=sys.maxsize
        if(coins[ind]<=amount):
            pick=1+self.helper(ind,coins,amount-coins[ind],n,dp)
        dp[ind][amount]=min(pick,notpick)
        return dp[ind][amount]
      